import requests
url = "https://api.github.com/users/dhanashyampmkd10-ai"
response = requests.get(url)
data = response.json()
print("=== GitHub User Info ===")
print(f"Name        : {data['name']}")
print(f"Location    : {data['location']}")
print(f"Public Repos: {data['public_repos']}")
print(f"Created At  : {data['created_at']}")