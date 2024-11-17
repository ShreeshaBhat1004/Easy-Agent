# agents/web_browsing_agent.py
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from groq import Groq

from .base_agent import BaseAgent

class WebBrowsingAgent(BaseAgent):
    def __init__(self, name, manager, api_key, search_api_key=None, search_engine_id=None, **kwargs):
        super().__init__(name, manager, **kwargs)
        self.api_key = api_key
        self.search_api_key = search_api_key
        self.search_engine_id = search_engine_id
        self.client = Groq(api_key=self.api_key)

    def receive_task(self, task):
        """
        Handle 'search' tasks.
        Task format: {'type': 'search', 'query': '...'}
        """
        if task.get('type') == 'search':
            query = task.get('query')
            results = self.search_web(query)
            if not results:
                summary = 'No results found.'
            else:
                summary = self.summarize_results(results)
            self.send_result({'task': task, 'summary': summary})
        else:
            self.send_result({'error': f"Unknown task type: {task.get('type')}"})

    def search_web(self, query, num_results=3):
        """
        Perform a web search using Google Custom Search API or fallback to googlesearch.
        """
        if self.search_api_key and self.search_engine_id:
            try:
                url = (
                    f"https://www.googleapis.com/customsearch/v1"
                    f"?key={self.search_api_key}&cx={self.search_engine_id}&q={query}&num={num_results}"
                )
                response = requests.get(url)
                response.raise_for_status()
                results = response.json().get('items', [])
                urls = [{'url': item['link'], 'snippet': item.get('snippet', '')} for item in results]
                return urls
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred during search: {http_err}")  # Log the error
                return []
            except Exception as e:
                print(f"An error occurred during search: {e}")  # Log the error
                return []
        else:
            try:
                search_results = list(search(query, num_results=num_results))
                return [{'url': url, 'snippet': 'Snippet unavailable.'} for url in search_results]
            except Exception as e:
                print(f"Fallback Search error: {str(e)}")
                return []

    def summarize_results(self, results):
        """
        Summarize search results into a coherent paragraph using Groq API.
        """
        if not results:
            return "No results found."

        combined_snippets = "\n".join([f"Source: {res['url']}\n{res['snippet']}" for res in results])
        summary_prompt = (
            "Based on the following information, provide a concise and coherent paragraph answering the question.\n\n"
            f"{combined_snippets}\n\n"
            "Answer:"
        )
        try:
            conversation = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": summary_prompt}
            ]
            response = self.client.chat.completions.create(
                messages=conversation,
                model="llama3-8b-8192",
                max_tokens=500,
                temperature=0.7,
            )
            paragraph = response.choices[0].message.content.strip()
            return paragraph
        except Exception as e:
            print(f"Summarization error: {str(e)}")
            return f"Summarization error: {str(e)}"
