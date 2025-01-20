import openai
from app.models.requirements import IdeaRequest, GeneratedRequirement
from app.repositories.mongodb import save_to_mongodb
from app.repositories.pinecone import store_embedding
from app.repositories.postgresql import index_in_postgres

openai.api_key = "your-openai-api-key"

def generate_requirements(request: IdeaRequest) -> GeneratedRequirement:
    # Generate requirements using OpenAI GPT
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Generate epics and user stories based on this idea: {request.idea_description}",
        max_tokens=500
    )
    generated_text = response.choices[0].text.strip()

    # Save to MongoDB and index in Pinecone and PostgreSQL
    save_to_mongodb(request.idea_description, generated_text)
    store_embedding(generated_text)
    index_in_postgres(generated_text)

    return GeneratedRequirement(idea=request.idea_description, requirements=generated_text)
