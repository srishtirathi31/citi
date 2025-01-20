from pydantic import BaseModel

class DesignRequest(BaseModel):
    requirements: str

class DesignResponse(BaseModel):
    mermaid_code: str
