import requests
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
joke = response.json()
print("=== Random Joke ===")
print("Setup     :", joke["setup"])
print("Punchline :", joke["punchline"])