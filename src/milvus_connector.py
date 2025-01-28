from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection
from pymilvus.orm import utility
from sentence_transformers import SentenceTransformer, util

from src.constants import JOKE_SENTENCE
from src.milvus_params import SEARCH_PARAMS, INDEX_PARAMS


class MilvusConnector:
    def __init__(self, host="localhost", port="19530", collection_name="jokes"):
        self.host = host
        self.port = port
        self.collection_name = collection_name
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embedding = self.model.encode(JOKE_SENTENCE, convert_to_tensor=True)
        self.threshold = 0.5

    def connect(self):
        connections.connect("default", host=self.host, port=self.port)
        print(f"Vector DB Connected at {self.host}:{self.port}")

    def create_collection(self) -> Collection:
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),
            FieldSchema(name="response", dtype=DataType.VARCHAR, max_length=500),
        ]
        schema = CollectionSchema(fields, description="Jokes Collection")
        collection = Collection(name=self.collection_name, schema=schema)
        return collection

    def get_or_create_collection(self) -> Collection:
        if utility.has_collection(self.collection_name):
            return Collection(self.collection_name)
        return self.create_collection()

    def add_joke(self, joke: str, predefined_message: str):
        collection = self.get_or_create_collection()
        embedding = self.model.encode(joke).tolist()
        data = [[embedding], [predefined_message]]
        collection.insert(data)
        self.create_index()
        print("Joke added to Vector DB \n")

    def create_index(self):
        collection = self.get_or_create_collection()
        collection.create_index(field_name="embedding", index_params=INDEX_PARAMS)
        print("Index created for collection. \n")

    def search_response(self, joke: str) -> str:
        collection = self.get_or_create_collection()
        embedding = self.model.encode(joke).tolist()
        collection.load()
        results = collection.search(
            [embedding], "embedding", param=SEARCH_PARAMS, limit=1, output_fields=["response"]
        )
        if results:
            return results[0][0].entity.get("response")
        return "No response found."

    def is_relevant_query(self, sentence):
        sentence_embedding = self.model.encode(sentence, convert_to_tensor=True)
        similarity = util.cos_sim(sentence_embedding, self.embedding)
        return similarity >= self.threshold


