# Manus API Python Task Creation Example

This repository contains a Python script that demonstrates how to create a new task using the [Manus API](https://open.manus.ai/docs). The script uses a `.env` file to securely manage your API key.

## Description

The `create_task.py` script sends a POST request to the `/v1/tasks` endpoint of the Manus API with a predefined prompt. It's a simple yet practical example for developers looking to get started with Manus API integrations in Python.

## Prerequisites

- Python 3.6+
- `pip` for installing packages

## Setup and Usage

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies:**
    The script requires the `requests` and `python-dotenv` libraries. Install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure your API Key:**
    -   Create a copy of the example environment file and name it `.env`:
        ```bash
        cp .env.example .env
        ```
    -   Open the `.env` file and replace `"your_actual_api_key_here"` with your real Manus API key.
        ```
        MANUS_API_KEY="your_actual_api_key_here"
        ```

4.  **Run the script:**
    Execute the script from your terminal:
    ```bash
    python create_task.py
    ```

If successful, the script will print a "Task created successfully!" message along with the JSON response from the API, which includes the new task's ID and URL.

## Manus API Documentation

For more detailed information about the API, including all available endpoints and parameters, please refer to the official [Manus API Documentation](https://open.manus.ai/docs).