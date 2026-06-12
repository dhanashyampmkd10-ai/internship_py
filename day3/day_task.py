import requests
from typing import Dict, Tuple
def fetch_user(username: str) -> Dict:
    try:
        url: str = f"https://api.github.com/users/{username}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Error: Unable to fetch GitHub user data.")
        return {}


def fetch_joke() -> Tuple[str, str]:
    try:
        url: str = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["setup"], data["punchline"]
    except requests.exceptions.RequestException:
        print("Error: Unable to fetch joke.")
        return "No joke available", "Try again later"


def display_user(user: Dict) -> None:
    if not user:
        print("No user data to display.")
        return
    print("\n=== GitHub User Card ===")
    print(f"Name        : {user.get('name')}")
    print(f"Username    : {user.get('login')}")
    print(f"Location    : {user.get('location')}")
    print(f"Public Repos: {user.get('public_repos')}")
    print(f"Created At  : {user.get('created_at')}")

def main() -> None:
    print("\n===== API EXPLORER =====")
    username: str = input("Enter GitHub username: ")
    user_data: Dict = fetch_user(username)
    display_user(user_data)
    setup, punchline = fetch_joke()
    print("\n=== Random Joke ===")
    print("Setup     :", setup)
    print("Punchline :", punchline)
if __name__ == "__main__":
    main()