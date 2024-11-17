# agents/reporting_agent.py
from .base_agent import BaseAgent

class ReportingAgent(BaseAgent):
    def receive_task(self, task):
        """
        Handle 'generate_report' tasks.
        Task format: {'type': 'generate_report', 'content': '...'}
        """
        if task.get('type') == 'generate_report':
            content = task.get('content')
            report = self.generate_report(content)
            self.send_result({'task': task, 'report': report})
        else:
            self.send_result({'error': f"Unknown task type: {task.get('type')}"})

    def generate_report(self, content):
        """
        Generate a report based on the provided content.
        """
        # Placeholder for report generation logic
        return f"Report Generated: {content}"
