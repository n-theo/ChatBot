import requests


class JokeFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_joke(self) -> str:
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                data = response.json()
                return f"{data['setup']} {data['punchline']}"
            return f"Error: Received status code {response.status_code} from API."
        except requests.RequestException as e:
            return f"Error: Could not fetch joke. Details: {str(e)}"
