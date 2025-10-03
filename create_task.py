import os
import requests
import json
from dotenv import load_dotenv

# This script sends a request to the Manus API to create a new task.
#
# Usage:
# 1. Install the required Python libraries:
#    pip install requests python-dotenv
# 2. Create a file named .env in the same directory as this script.
# 3. Add your Manus API key to the .env file like this:
#    MANUS_API_KEY="your_actual_api_key_here"
# 4. Run the script from your terminal:
#    python create_task.py

def create_manus_task():
    """
    Creates a new task in Manus using the API.
    """
    # Load environment variables from the .env file
    load_dotenv()

    # Get the API key from environment variables
    api_key = os.environ.get("MANUS_API_KEY")

    if not api_key:
        print("Error: MANUS_API_KEY not found.")
        print("Please make sure you have a .env file with your API key.")
        return

    # The prompt for the new task
    prompt = "AIニュース調べて"

    # API endpoint for creating tasks
    url = "https://api.manus.ai/v1/tasks"

    # Headers for the request
    headers = {
        "API_KEY": api_key,
        "Content-Type": "application/json"
    }

    # Data payload for the request
    data = {
        "prompt": prompt
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Print the successful response
        print("Task created successfully!")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        if e.response:
            print(f"Response content: {e.response.text}")

if __name__ == "__main__":
    create_manus_task()