# scripts/interactive_run.py
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from agents.agent_manager import AgentManager
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Define the path to the configuration file
    config_path = os.path.join(os.path.dirname(__file__), '../config/agents_config.yaml')

    # Initialize Agent Manager
    manager = AgentManager(config_path)

    print("Multi-Agent System is running. Enter commands to interact.")
    print("Commands:")
    print("1. search <your query>")
    print("2. process <your data>")
    print("3. report <your content>")
    print("4. exit")

    while True:
        user_input = input(">> ").strip()
        if user_input.lower() == 'exit':
            print("Shutting down the system. Goodbye!")
            break
        elif user_input.lower().startswith('search '):
            query = user_input[7:]
            task = {'type': 'search', 'query': query}
            manager.add_task(task)
        elif user_input.lower().startswith('process '):
            data = user_input[8:]
            task = {'type': 'process_data', 'data': data}
            manager.add_task(task)
        elif user_input.lower().startswith('report '):
            content = user_input[7:]
            task = {'type': 'generate_report', 'content': content}
            manager.add_task(task)
        else:
            print("Unknown command. Please try again.")
            continue

        # Assign and execute tasks
        manager.assign_tasks()

        # Retrieve and display results
        results = manager.get_results()
        print("\nCurrent Results:")
        for agent, result in results.items():
            print(f"Agent: {agent}\nResult: {result}\n")

if __name__ == "__main__":
    main()
