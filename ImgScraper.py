import requests
from bs4 import BeautifulSoup
import os

# User input for the URL
url = input("Enter the URL of the webpage: ")

# Send an HTTP GET request to the webpage
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all image tags (<img>) in the parsed HTML
image_tags = soup.find_all("img")

# Create a directory to store the downloaded images
output_dir = "Images"  # Name of the directory to store images
os.makedirs(output_dir, exist_ok=True)

# Iterate over the image tags, download the images, and save them locally
for img in image_tags:
    src = img.get("src")
    if src is not None and src.startswith("http"):  # Check if the src is a valid URL
        image_url = src
        response = requests.get(image_url)
        if response.status_code == 200:
            # Extract the image file name
            image_name = image_url.split("/")[-1]
            image_path = os.path.join(output_dir, image_name)
            # Save the image to the local directory
            with open(image_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded: {image_name}")
