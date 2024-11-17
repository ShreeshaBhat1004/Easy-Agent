# agents/data_processing_agent.py
from .base_agent import BaseAgent

class DataProcessingAgent(BaseAgent):
    def receive_task(self, task):
        """
        Handle 'process_data' tasks.
        Task format: {'type': 'process_data', 'data': '...'}
        """
        if task.get('type') == 'process_data':
            data = task.get('data')
            processed_data = self.process_data(data)
            self.send_result({'task': task, 'processed_data': processed_data})
        else:
            self.send_result({'error': f"Unknown task type: {task.get('type')}"})

    def process_data(self, data):
        """
        Process the data as required.
        """
        # Placeholder for data processing logic
        return f"Processed data: {data}"
