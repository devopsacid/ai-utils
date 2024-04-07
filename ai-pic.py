import requests

# load OPENAI_KEY from .env file
from dotenv import load_dotenv
load_dotenv
import os
OPENAI_KEY = os.getenv('OPENAI_KEY')

# Image analysis API URL
image_analysis_url = "https://api.example.com/v1/analyze-image"

# load image_path from arguments
import sys
image_path = sys.argv[1]

# The path to the image file you want to analyze
# image_path = 'path/to/your/image.jpg'

# Set up headers, if any. This may include your API key and other necessary headers.
headers = {
    "Authorization": f"Bearer {OPENAI_KEY}",
}

# Depending on the API requirements, you may have to send the image as JSON data,
# form data, or directly as files. Here is an example using multipart/form-data:
files = {"file": (image_path, open(image_path, "rb"), "image/jpeg")}

# Send a POST request
response = requests.post(image_analysis_url, headers=headers, files=files)

# Check if the request was successful and print the response
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)
