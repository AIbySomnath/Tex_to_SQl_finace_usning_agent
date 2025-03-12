# Financial Data Analysis with AI Agents

## Overview

This project demonstrates the development of AI agents using an LLM-based framework to process financial data. The agents work together to process a command, generate an appropriate SQL query, execute it on a database, and return the result along with a summary. The application also includes a Streamlit interface for user interaction.

## Files

- `agent1.py`: Implementation of Agent 1.
- `database_developer_agent.py`: Translates natural language queries into SQL queries.
- `data_analyst_agent.py`: Analyzes the SQL query results to extract patterns and insights.
- `report_writer_agent.py`: Summarizes the findings into a concise, readable report.
- `database.py`: Handles the database setup and connection.
- `sql_tool.py`: Defines the SQL execution tool.
- `model.py`: Contains the model configuration.
- `main.py`: Entry point to run the agents.
- `app.py`: Streamlit application for user interaction.
- `requirements.txt`: Lists the required dependencies.
- `Dockerfile`: Defines the Docker setup for the project.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Setup

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the main script:
    ```bash
    python main.py
    ```

3. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Docker

To build and run the project using Docker, follow these steps:

1. Build the Docker image:
    ```bash
    docker build -t ai-agents .
    ```

2. Run the Docker container:
    ```bash
    docker run -it ai-agents
    ```

## Model and Approach

### Text-to-SQL Agent with Deepseek R1

The project uses the Deepseek R1 model to translate natural language queries into SQL queries. This approach allows the AI agents to process user commands, generate appropriate SQL queries, execute them on the database, and return the results along with a summary.



Sample data is inserted into the database to simulate financial transactions similar to L&T Finance data.

### AI Agents

1. **Database Developer Agent**: Constructs and executes SQL queries based on natural language input.
2. **Data Analyst Agent**: Analyzes the query results to extract patterns and insights.
3. **Report Writer Agent**: Summarizes the findings into a concise, readable report.

## License

This project is licensed under the MIT License.
