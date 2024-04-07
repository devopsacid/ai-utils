from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_API_KEY')

headers = {
    "Authorization": f"Bearer {OPENAI_KEY}",
}

client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="create schema of electric circuit integrating x86 chip into a motherboard",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

# get picture from URL
import requests
from PIL import Image
from io import BytesIO

response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
# img.show()

# Save the image to a file
img.save("x86_integration.jpg")
