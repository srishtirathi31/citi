from pydantic import BaseModel

class UserStoryRequest(BaseModel):
    user_story: str
    repo_name: str

class CodeGenerationResponse(BaseModel):
    generated_code: str
    github_pr_url: str
