# scripts/run_system.py
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
from agents.agent_manager import AgentManager
from dotenv import load_dotenv


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Optional: Print environment variables for debugging
    print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))
    print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))
    print("GOOGLE_CX:", os.getenv("GOOGLE_CX"))

    # Define the path to the configuration file
    config_path = os.path.join(os.path.dirname(__file__), '../config/agents_config.yaml')

    # Initialize Agent Manager
    manager = AgentManager(config_path)

    # Example Task Flow
    # 1. Search for latest presidential election results
    search_task = {'type': 'search', 'query': 'who won the 2024 presidential elections'}
    manager.add_task(search_task)

    # 2. Process the search results
    process_task = {'type': 'process_data', 'data': 'Election results data'}
    manager.add_task(process_task)

    # 3. Generate a report based on processed data
    report_task = {'type': 'generate_report', 'content': 'Summary of the 2024 presidential election results.'}
    manager.add_task(report_task)

    # Assign and execute tasks
    manager.assign_tasks()

    # Retrieve and display results
    results = manager.get_results()
    print("\nFinal Results:")
    for agent, result in results.items():
        print(f"Agent: {agent}\nResult: {result}\n")

if __name__ == "__main__":
    main()
