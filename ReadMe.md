
 <!-- Replace with your project's logo if available -->
![Your SVG description](https://github.com/ShreeshaBhat1004/MALWARE-ANALYSIS/blob/main/easy-agent--a-logo-related-to-ai.svg) {
width:50%; }
## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)

- [Installation](#installation)
- [Configuration](#configuration)
  - [Setting Up API Keys](#setting-up-api-keys)
- [Running the System](#running-the-system)
- [Creating Custom Agents](#creating-custom-agents)
  - [Agent Structure](#agent-structure)
  - [Implementing a New Agent](#implementing-a-new-agent)
  - [Registering the New Agent](#registering-the-new-agent)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

**Easy-Agent** is a versatile multi-agent system designed to perform a variety of tasks by leveraging specialized agents. Built with modularity and extensibility in mind, Easy-Agent allows developers to create, integrate, and manage custom agents effortlessly. Whether you need web browsing capabilities, data processing, reporting, or other functionalities, Easy-Agent provides a robust framework to meet your needs.

## Features

- **Modular Architecture**: Easily add or remove agents without affecting the overall system.
- **Custom Agent Support**: Develop and integrate your own agents tailored to specific tasks.
- **API Integration**: Seamlessly connect with external APIs like Google Custom Search and Groq for enhanced functionalities.
- **Environment Variable Management**: Securely manage sensitive information using `.env` files.
- **Comprehensive Logging**: Monitor system operations and debug with detailed logs.
- **Task Queue Management**: Efficiently handle and assign tasks to appropriate agents.
- **Flexible Configuration**: Customize agent behaviors and system settings through YAML configurations.

## Prerequisites

Before setting up Easy-Agent, ensure you have the following installed on your system:

- **Python 3.7 or higher**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Virtual Environment (optional but recommended)**: While not mandatory, using a virtual environment helps manage dependencies effectively.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/Easy-Agent.git
   cd Easy-Agent
   ```

2. **Set Up a Virtual Environment (Recommended)**

   ```bash
   python -m venv venv
   ```

   - **Activate the Virtual Environment:**
     - **On Windows:**
       ```bash
       venv\Scripts\activate
       ```
     - **On macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Easy-Agent utilizes environment variables to manage sensitive information like API keys. Follow the steps below to configure the system properly.

### Setting Up API Keys

1. **Obtain API Keys**

   - **Groq API Key (`GROQ_API_KEY`)**: Register and obtain your Groq API key from the [Groq Developer Portal](https://groq.com/developers).
   - **Google Custom Search API Key (`GOOGLE_API_KEY`)**: Acquire your Google API key from the [Google Cloud Console](https://console.cloud.google.com/).
   - **Google Custom Search Engine ID (`GOOGLE_CX`)**: Create a Custom Search Engine (CSE) and obtain the `cx` identifier from the [Google Programmable Search Engine](https://programmablesearchengine.google.com/).

2. **Create a `.env` File**

   In the root directory of the project (`Easy-Agent/`), create a file named `.env` and add your API keys as follows:

   ```env
   # .env
   GROQ_API_KEY=your_actual_groq_api_key_here
   GOOGLE_API_KEY=your_actual_google_api_key_here
   GOOGLE_CX=your_actual_google_cx_here
   ```

   **Notes:**
   - **Security**: Ensure that `.env` is included in your `.gitignore` to prevent accidental commits of sensitive information.
   - **Format**: Do not enclose values in quotes unless necessary. Avoid spaces around the `=` sign.

3. **Configure Agents**

   The agent configurations are defined in `config/agents_config.yaml`. Ensure that the placeholders correspond to your `.env` variables.

   ```yaml
   # config/agents_config.yaml
   agents:
     - name: WebBrowsingAgent
       type: web_browsing
       params:
         api_key: "${GROQ_API_KEY}"
         search_api_key: "${GOOGLE_API_KEY}"
         search_engine_id: "${GOOGLE_CX}"
   
     - name: DataProcessingAgent1
       type: data_processing
       params: {}
   
     - name: ReportingAgent1
       type: reporting
       params: {}
   ```

   **Customization:**
   - **Adding More Agents**: You can add more agents by appending entries to the `agents` list.
   - **Parameterization**: Define specific parameters for each agent type as needed.

## Running the System

To execute the multi-agent system, use the provided scripts. Here's how to run the main system:

1. **Navigate to the Project Root**

   Ensure you're in the `Easy-Agent/` directory.

   ```bash
   cd Easy-Agent
   ```

2. **Run the Main Script**

   ```bash
   python scripts/run_system.py
   ```

   **What It Does:**
   - **Loads Configuration**: Reads `agents_config.yaml` and initializes agents.
   - **Loads Environment Variables**: Reads API keys from the `.env` file.
   - **Adds Tasks**: Queues predefined tasks for agents to process.
   - **Assigns and Executes Tasks**: Delegates tasks to the appropriate agents.
   - **Displays Results**: Prints the final outcomes of each agent's operations.

3. **Example Output**

   ```
   GROQ_API_KEY: your_actual_groq_api_key_here
   GOOGLE_API_KEY: your_actual_google_api_key_here
   GOOGLE_CX: your_actual_google_cx_here
   2024-04-27 12:00:00,000 - agents.agent_manager - INFO - Replaced api_key with environment variable GROQ_API_KEY: your_actual_groq_api_key_here
   2024-04-27 12:00:00,100 - agents.agent_manager - INFO - Replaced search_api_key with environment variable GOOGLE_API_KEY: your_actual_google_api_key_here
   2024-04-27 12:00:00,200 - agents.agent_manager - INFO - Replaced search_engine_id with environment variable GOOGLE_CX: your_actual_google_cx_here
   2024-04-27 12:00:00,300 - agents.agent_manager - INFO - Agent 'WebBrowsingAgent' of type 'web_browsing' registered.
   2024-04-27 12:00:00,400 - agents.agent_manager - INFO - Agent 'DataProcessingAgent1' of type 'data_processing' registered.
   2024-04-27 12:00:00,500 - agents.agent_manager - INFO - Agent 'ReportingAgent1' of type 'reporting' registered.
   2024-04-27 12:00:00,600 - agents.agent_manager - INFO - Task added: {'type': 'search', 'query': 'who won the 2024 presidential elections'}
   2024-04-27 12:00:00,700 - agents.agent_manager - INFO - Task added: {'type': 'process_data', 'data': 'Election results data'}
   2024-04-27 12:00:00,800 - agents.agent_manager - INFO - Task added: {'type': 'generate_report', 'content': 'Summary of the 2024 presidential election results.'}
   2024-04-27 12:00:00,900 - agents.agent_manager - INFO - Assigning task {'type': 'search', 'query': 'who won the 2024 presidential elections'} to agent 'WebBrowsingAgent'.
   2024-04-27 12:00:01,000 - agents.web_browsing_agent - INFO - Performing search with URL: https://www.googleapis.com/customsearch/v1?key=your_actual_google_api_key_here&cx=your_actual_google_cx_here&q=who+won+the+2024+presidential+elections&num=3
   2024-04-27 12:00:01,100 - agents.web_browsing_agent - INFO - Retrieved 3 results from Google Custom Search API.
   2024-04-27 12:00:01,200 - agents.web_browsing_agent - INFO - Sending prompt to Groq API for summarization.
   2024-04-27 12:00:01,300 - agents.web_browsing_agent - INFO - Received summary from Groq API.
   2024-04-27 12:00:01,400 - agents.agent_manager - INFO - Result received from 'WebBrowsingAgent': {'task': {'type': 'search', 'query': 'who won the 2024 presidential elections'}, 'summary': 'In the 2024 United States presidential election, [Candidate Name] secured victory over [Opponent Name], garnering a significant majority of both the popular and electoral votes. This outcome reflects [brief analysis based on fetched data]. For more detailed results and insights, please refer to reputable news sources.'}
   2024-04-27 12:00:01,500 - agents.agent_manager - INFO - Assigning task {'type': 'process_data', 'data': 'Election results data'} to agent 'DataProcessingAgent1'.
   2024-04-27 12:00:01,600 - agents.data_processing_agent - INFO - Processing data: Election results data
   2024-04-27 12:00:01,700 - agents.data_processing_agent - INFO - Processed data: Election results data
   2024-04-27 12:00:01,800 - agents.agent_manager - INFO - Result received from 'DataProcessingAgent1': {'task': {'type': 'process_data', 'data': 'Election results data'}, 'processed_data': 'Processed data: Election results data'}
   2024-04-27 12:00:01,900 - agents.agent_manager - INFO - Assigning task {'type': 'generate_report', 'content': 'Summary of the 2024 presidential election results.'} to agent 'ReportingAgent1'.
   2024-04-27 12:00:02,000 - agents.reporting_agent - INFO - Generating report: Summary of the 2024 presidential election results.
   2024-04-27 12:00:02,100 - agents.reporting_agent - INFO - Report Generated: Summary of the 2024 presidential election results.
   
   Final Results:
   Agent: WebBrowsingAgent
   Result: {'task': {'type': 'search', 'query': 'who won the 2024 presidential elections'}, 'summary': 'In the 2024 United States presidential election, [Candidate Name] secured victory over [Opponent Name], garnering a significant majority of both the popular and electoral votes. This outcome reflects [brief analysis based on fetched data]. For more detailed results and insights, please refer to reputable news sources.'}
   
   Agent: DataProcessingAgent1
   Result: {'task': {'type': 'process_data', 'data': 'Election results data'}, 'processed_data': 'Processed data: Election results data'}
   
   Agent: ReportingAgent1
   Result: {'task': {'type': 'generate_report', 'content': 'Summary of the 2024 presidential election results.'}, 'report': 'Report Generated: Summary of the 2024 presidential election results.'}
   ```

## Creating Custom Agents

One of Easy-Agent's strengths is its ability to incorporate custom agents tailored to specific tasks. Follow the steps below to create and integrate your own agents seamlessly.

### Agent Structure

Each agent should be a Python class inheriting from a base agent class (e.g., `BaseAgent`). The agent must implement necessary methods to handle tasks, process data, and communicate with other components.

**Example Base Agent:**

```python
# agents/base_agent.py
import logging

class BaseAgent:
    def __init__(self, name, manager, **kwargs):
        self.name = name
        self.manager = manager
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)
    
    def receive_task(self, task):
        """
        Handle incoming tasks.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
    def send_result(self, result):
        """
        Send results back to the manager.
        """
        self.manager.receive_result(self.name, result)
```

### Implementing a New Agent

1. **Create the Agent File**

   In the `agents/` directory, create a new Python file for your agent. For example, `image_processing_agent.py`.

   ```python
   # agents/image_processing_agent.py
   from .base_agent import BaseAgent
   import logging

   class ImageProcessingAgent(BaseAgent):
       def __init__(self, name, manager, **kwargs):
           super().__init__(name, manager, **kwargs)
           # Initialize any additional parameters or resources here

       def receive_task(self, task):
           """
           Handle 'process_image' tasks.
           Task format: {'type': 'process_image', 'image_path': 'path/to/image.jpg'}
           """
           if task.get('type') == 'process_image':
               image_path = task.get('image_path')
               self.logger.info(f"Processing image: {image_path}")
               # Implement image processing logic here
               processed_data = f"Processed image at {image_path}"
               self.send_result({'task': task, 'processed_data': processed_data})
           else:
               error_msg = f"Unknown task type: {task.get('type')}"
               self.logger.error(error_msg)
               self.send_result({'error': error_msg})
   ```

2. **Register the New Agent**

   Update `config/agents_config.yaml` to include your new agent.

   ```yaml
   # config/agents_config.yaml
   agents:
     - name: WebBrowsingAgent
       type: web_browsing
       params:
         api_key: "${GROQ_API_KEY}"
         search_api_key: "${GOOGLE_API_KEY}"
         search_engine_id: "${GOOGLE_CX}"
   
     - name: DataProcessingAgent1
       type: data_processing
       params: {}
   
     - name: ReportingAgent1
       type: reporting
       params: {}
   
     - name: ImageProcessingAgent1
       type: image_processing
       params:
         # Add any specific parameters your agent requires
   ```

3. **Update `AgentManager` to Support the New Agent Type**

   Modify `agents/agent_manager.py` to recognize the new `image_processing` type.

   ```python
   # agents/agent_manager.py
   # Add the import for the new agent
   from .image_processing_agent import ImageProcessingAgent
   
   class AgentManager:
       # ... existing code ...
   
       def load_agents(self, config_path):
           # ... existing code ...
   
                   if agent_type == 'web_browsing':
                       agent = WebBrowsingAgent(name, self, **params)
                   elif agent_type == 'data_processing':
                       agent = DataProcessingAgent(name, self, **params)
                   elif agent_type == 'reporting':
                       agent = ReportingAgent(name, self, **params)
                   elif agent_type == 'image_processing':
                       agent = ImageProcessingAgent(name, self, **params)
                   else:
                       logger.error(f"Unknown agent type: {agent_type}")
                       continue
   
           # ... existing code ...
   
       def get_supported_tasks(self, agent):
           if isinstance(agent, WebBrowsingAgent):
               return ['search']
           elif isinstance(agent, DataProcessingAgent):
               return ['process_data']
           elif isinstance(agent, ReportingAgent):
               return ['generate_report']
           elif isinstance(agent, ImageProcessingAgent):
               return ['process_image']
           else:
               return []
   ```

4. **Use the New Agent**

   You can now add tasks for your new agent. For example, in `run_system.py`:

   ```python
   # scripts/run_system.py
   def main():
       # ... existing code ...
   
       # 4. Process an image
       image_task = {'type': 'process_image', 'image_path': 'path/to/image.jpg'}
       manager.add_task(image_task)
   
       # Assign and execute tasks
       manager.assign_tasks()
   
       # ... existing code ...
   ```

### Registering the New Agent

Ensure that the `AgentManager` is aware of the new agent type by updating both the import statements and the conditional logic that instantiates agents based on their type. This ensures seamless integration and task assignment.

## Project Structure

Understanding the project's directory structure is crucial for navigating and extending the system.

```
Easy-Agent/
├── agents/
│   ├── __init__.py
│   ├── agent_manager.py
│   ├── base_agent.py
│   ├── web_browsing_agent.py
│   ├── data_processing_agent.py
│   ├── reporting_agent.py
│   └── image_processing_agent.py
├── config/
│   └── agents_config.yaml
├── scripts/
│   ├── __init__.py
│   ├── run_system.py
│   └── interactive_run.py
├── requirements.txt
├── .env
└── README.md
```

**Descriptions:**

- **agents/**: Contains all agent classes and related modules.
  - `__init__.py`: Makes the directory a Python package.
  - `agent_manager.py`: Manages agents, task assignment, and result collection.
  - `base_agent.py`: Defines the base class for all agents.
  - `web_browsing_agent.py`: Agent for performing web searches.
  - `data_processing_agent.py`: Agent for processing data.
  - `reporting_agent.py`: Agent for generating reports.
  - `image_processing_agent.py`: (Example) Agent for processing images.

- **config/**: Holds configuration files.
  - `agents_config.yaml`: Defines agents and their parameters.

- **scripts/**: Contains executable scripts.
  - `__init__.py`: Makes the directory a Python package.
  - `run_system.py`: Main script to run the multi-agent system.
  - `interactive_run.py`: (Optional) Script for interactive task management.

- **requirements.txt**: Lists all Python dependencies.

- **.env**: Stores environment variables and API keys.

- **README.md**: Project documentation (this file).

## Troubleshooting

Encountering issues is a natural part of development. Here are some common problems and their solutions.

### 1. `ModuleNotFoundError: No module named 'agents'`

**Cause:** Python cannot locate the `agents` module due to incorrect project structure or import statements.

**Solution:**

- **Ensure `__init__.py` Exists:**
  - Verify that the `agents/` directory contains an `__init__.py` file.

- **Correct Import Paths:**
  - Use absolute imports in your scripts.
  - Add the project root to `sys.path` if necessary.

- **Run Scripts from Project Root:**
  - Navigate to the `Easy-Agent/` directory before executing scripts.

- **Use the `-m` Flag:**
  - Run scripts as modules to help Python resolve imports.
    ```bash
    python -m scripts.run_system
    ```

### 2. `AttributeError: 'AgentManager' object has no attribute 'add_task'`

**Cause:** The `AgentManager` class lacks the `add_task` method or there is a typo in the method name.

**Solution:**

- **Verify Method Definition:**
  - Ensure `add_task` is defined in `agent_manager.py`.

- **Check for Typos:**
  - Confirm consistent naming (`add_task` vs. `addTasks`).

- **Review Class Instantiation:**
  - Make sure you're instantiating the correct `AgentManager` class.

### 3. API Errors (e.g., `400 Bad Request`)

**Cause:** Malformed API requests due to incorrect API keys, CSE ID, or misconfigurations.

**Solution:**

- **Verify `.env` File:**
  - Ensure API keys are correctly set without typos.
  
- **Check CSE Configuration:**
  - Confirm that your Custom Search Engine is set to search the entire web.
  
- **Test APIs Independently:**
  - Use separate scripts to validate API functionality.

- **Monitor API Quotas and Billing:**
  - Ensure you haven't exceeded usage limits and billing is enabled.

### 4. No Results Found

**Cause:** The search query might be too specific, or the API isn't returning results due to configuration issues.

**Solution:**

- **Use General Queries:**
  - Test with broader search terms to verify functionality.

- **Inspect API Responses:**
  - Enable detailed logging to view API response content.

- **Ensure Proper API Configuration:**
  - Double-check that the API keys and CSE ID are correct and active.

## Contributing

Contributions are welcome! If you'd like to enhance Easy-Agent, please follow these guidelines:

1. **Fork the Repository**

   Click the "Fork" button at the top-right corner of this page.

2. **Create a New Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**

   Implement your feature, fix bugs, or improve documentation.

4. **Commit Your Changes**

   ```bash
   git commit -m "Add feature: your feature description"
   ```

5. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Submit a Pull Request**

   Navigate to the original repository and click "New pull request".

**Please ensure your contributions adhere to the project's coding standards and include relevant tests.**

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer:** Replace placeholder text like `yourusername`, `path_to_logo_image`, and `your_actual_api_key_here` with your actual information. Ensure sensitive information like API keys are never committed to version control systems.

---

**Contact Information:**

For any questions, suggestions, or support, feel free to reach out:

- **Email:** your.email@example.com
- **GitHub Issues:** [Open an Issue](https://github.com/yourusername/Easy-Agent/issues)
- **Twitter:** [@yourtwitterhandle](https://twitter.com/yourtwitterhandle)

Happy Coding! 🚀
