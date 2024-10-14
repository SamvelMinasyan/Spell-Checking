import random
import re
import requests
import os


# Define some common misspelling rules (you can expand these)
def introduce_typos(word):
	if len(word) > 1:
		i = random.randint(0, len(word) - 2)
		return word[:i] + word[i + 1] + word[i] + word[i + 2:]  # Swap two letters
	return word


def generate_synthetic_data(text):
	words = text.split()
	synthetic_text = " ".join([introduce_typos(word) if random.random() < 0.1 else word for word in words])
	return synthetic_text


def fetch_and_prepare_data():
	# Fetching a simple text dataset from a URL
	url = "https://raw.githubusercontent.com/dscape/spell/master/test/resources/big.txt"  # Public text dataset
	response = requests.get(url)
	text_data = response.text if response.status_code == 200 else "Error: Failed to fetch dataset."

	text_data = text_data[:20000]

	# Introduce synthetic errors
	synthetic_data = generate_synthetic_data(text_data)

	# Save original and synthetic data
	os.makedirs("data/raw", exist_ok=True)
	with open("data/raw/original.txt", "w") as f:
		f.write(text_data)
	with open("data/raw/synthetic.txt", "w") as f:
		f.write(synthetic_data)

	print("Data preparation completed and saved in the data/raw directory.")


if __name__ == "__main__":
	fetch_and_prepare_data()
