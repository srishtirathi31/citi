import openai
from app.models.design import DesignRequest, DesignResponse

openai.api_key = "your-openai-api-key"

def generate_design(request: DesignRequest) -> DesignResponse:
    # Generate design using OpenAI GPT
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Generate a mermaid diagram for the following requirements: {request.requirements}",
        max_tokens=500
    )
    mermaid_code = response.choices[0].text.strip()
    
    return DesignResponse(mermaid_code=mermaid_code)
