import pinecone
from app.config import Config

pinecone.init(api_key=Config.PINECONE_API_KEY, environment="us-west1-gcp")
index = pinecone.Index("requirements")

def store_embedding(requirements: str):
    embedding = openai.Embedding.create(
        input=requirements, model="text-embedding-ada-002"
    )["data"][0]["embedding"]
    index.upsert([(str(requirements), embedding)])
