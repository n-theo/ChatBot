from milvus_connector import MilvusConnector
from joke_fetcher import JokeFetcher
from src.constants import API_URL, PREDEFINED_MESSAGE


def main():
    milvus_connector = MilvusConnector()
    joke_fetcher = JokeFetcher(url=API_URL)
    milvus_connector.connect()
    user_input = input("Enter a string (fetch joke || quit): ").strip().lower()
    if user_input == "fetch joke":
        joke = joke_fetcher.fetch_joke()
        print(f"Fetched Joke: {joke}")
        milvus_connector.add_joke(joke, PREDEFINED_MESSAGE)
        response = milvus_connector.search_response(joke)
        print(f"Response from Milvus: {response}")
        print(f"Joke: {joke}")
    if user_input == "quit":
        print("Bye Now")
    else:
        print("Input should be fetch joke || quit")


if __name__ == "__main__":
    main()
