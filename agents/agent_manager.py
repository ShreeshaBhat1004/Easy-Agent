# agents/agent_manager.py
import yaml
import os
import logging
from collections import deque

from .web_browsing_agent import WebBrowsingAgent
from .data_processing_agent import DataProcessingAgent
from .reporting_agent import ReportingAgent

# Configure logging for this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to ch
ch.setFormatter(formatter)

# Add ch to logger if not already added
if not logger.handlers:
    logger.addHandler(ch)

class AgentManager:
    def __init__(self, config_path):
        self.agents = {}
        self.task_queue = deque()
        self.results = {}
        self.load_agents(config_path)

    def load_agents(self, config_path):
        """
        Load agent configurations from a YAML file and instantiate agents.
        """
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
            
            for agent_cfg in config.get('agents', []):
                name = agent_cfg.get('name')
                agent_type = agent_cfg.get('type')
                params = agent_cfg.get('params', {})

                # Replace environment variable placeholders
                for key, value in params.items():
                    if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
                        var_name = value[2:-1]
                        params[key] = os.getenv(var_name, "")
                        logger.info(f"Replaced {key} with environment variable {var_name}: {params[key]}")

                if agent_type == 'web_browsing':
                    agent = WebBrowsingAgent(name, self, **params)
                elif agent_type == 'data_processing':
                    agent = DataProcessingAgent(name, self, **params)
                elif agent_type == 'reporting':
                    agent = ReportingAgent(name, self, **params)
                else:
                    logger.error(f"Unknown agent type: {agent_type}")
                    continue

                self.agents[name] = agent
                logger.info(f"Agent '{name}' of type '{agent_type}' registered.")
        except Exception as e:
            logger.error(f"Error loading agents configuration: {str(e)}")

    def add_task(self, task):
        """
        Add a task to the queue.
        """
        self.task_queue.append(task)
        logger.info(f"Task added: {task}")

    def assign_tasks(self):
        """
        Assign tasks to appropriate agents based on task type.
        """
        while self.task_queue:
            task = self.task_queue.popleft()
            task_type = task.get('type')
            agent = self.get_agent_for_task(task_type)
            if agent:
                logger.info(f"Assigning task {task} to agent '{agent.name}'.")
                agent.receive_task(task)
            else:
                logger.error(f"No suitable agent found for task type: {task_type}")

    def get_agent_for_task(self, task_type):
        """
        Retrieve the agent responsible for the given task type.
        """
        for agent in self.agents.values():
            if task_type in self.get_supported_tasks(agent):
                return agent
        return None

    def get_supported_tasks(self, agent):
        """
        Define supported tasks for each agent type.
        """
        if isinstance(agent, WebBrowsingAgent):
            return ['search']
        elif isinstance(agent, DataProcessingAgent):
            return ['process_data']
        elif isinstance(agent, ReportingAgent):
            return ['generate_report']
        else:
            return []

    def receive_result(self, agent_name, result):
        """
        Receive results from agents.
        """
        self.results[agent_name] = result
        logger.info(f"Result received from '{agent_name}': {result}")

    def get_results(self):
        """
        Retrieve all results.
        """
        return self.results
