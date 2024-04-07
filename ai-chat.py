import requests

# OpenAI API URL for GPT-3 model
openai_url = "https://api.openai.com/v1/engines/davinci-codex/completions"

# Set up your OpenAI API key
headers = {
    "Authorization": f"Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Data with the prompt for the API
data = {
    "prompt": "Once upon a time in a magical land, there lived a dragon...",
    "max_tokens": 100
}

# Send a POST request
response = requests.post(openai_url, headers=headers, json=data)

# Check if the request was successful and print the response
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)
