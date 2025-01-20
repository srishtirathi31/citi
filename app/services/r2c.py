import openai
from app.models.code import UserStoryRequest, CodeGenerationResponse
import requests

openai.api_key = "your-openai-api-key"

GITHUB_API_URL = "https://api.github.com/repos/your-repo/pulls"
GITHUB_TOKEN = "your-github-token"

def generate_code(request: UserStoryRequest) -> CodeGenerationResponse:
    # Generate code using OpenAI GPT
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Generate Python code for this user story: {request.user_story}",
        max_tokens=500
    )
    generated_code = response.choices[0].text.strip()

    # Create a Pull Request in GitHub
    pr_data = {
        "title": f"Code for user story: {request.user_story}",
        "head": "feature-branch",
        "base": "main",
        "body": generated_code
    }
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    pr_response = requests.post(GITHUB_API_URL, json=pr_data, headers=headers)
    
    if pr_response.status_code == 201:
        pr_url = pr_response.json()['html_url']
        return CodeGenerationResponse(generated_code=generated_code, github_pr_url=pr_url)
    else:
        return CodeGenerationResponse(generated_code=generated_code, github_pr_url="Error creating PR")
