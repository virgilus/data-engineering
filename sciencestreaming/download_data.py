import os
import requests

DATA_URL = "https://github.com/virgilus/data/raw/refs/heads/main/sciencestreaming/compressed/sciencestreaming.sql.gz"
SAVE_PATH = "data/compressed/sciencestreaming.sql.gz"

def download_data(url: str, save_path: str):
    """Download data from the specified URL and save it to the given path."""
    
    print(f"Downloading data from {url}...")
    print(f"And saving to {save_path}")
    
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an error for bad responses

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Data downloaded and saved to {save_path}")
    
if __name__ == "__main__":
    download_data(DATA_URL, SAVE_PATH)