# agents/base_agent.py
class BaseAgent:
    def __init__(self, name, manager, **kwargs):
        self.name = name
        self.manager = manager  # Reference to AgentManager
        self.params = kwargs    # Additional parameters

    def receive_task(self, task):
        """
        Receive a task from the manager.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def send_result(self, result):
        """
        Send the result back to the manager.
        """
        self.manager.receive_result(self.name, result)
