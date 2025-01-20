from pydantic import BaseModel

class IdeaRequest(BaseModel):
    idea_description: str

class GeneratedRequirement(BaseModel):
    idea: str
    requirements: str
