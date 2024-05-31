import os
import random
import requests
import subprocess
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Set the directory where the downloaded images will be stored
directory = Path.home() / "Developer/Bash/change-wallpaper"

# Set the file type for the images to be downloaded
file_type = "jpg"

NASA_API_KEY = os.getenv("NASA_TOKEN")

# Get a random image from Pexels API
response = requests.get(
    f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}",
)

# Extract the image URL from the API response
img_url = response.json()["hdurl"]

# Download the image
file_path = directory / f"background.{file_type}"
with requests.get(img_url, stream=True) as r:
    r.raise_for_status()
    with open(file_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# Set the downloaded image as the desktop wallpaper
script = f'tell application "System Events" to set picture of every desktop to "{file_path}"'
try:
    subprocess.run(["osascript", "-e", script], check=True)
    # Refresh the Dock
    subprocess.run(["killall", "Dock"])
    print("Desktop wallpaper changed successfully!")
except subprocess.CalledProcessError:
    print("Error: Desktop wallpaper could not be changed.")
