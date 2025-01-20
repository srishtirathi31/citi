from fastapi import APIRouter
from app.models.code import UserStoryRequest, CodeGenerationResponse
from app.services.r2c import generate_code

router = APIRouter()

@router.post("/generate_code", response_model=CodeGenerationResponse)
async def generate_code_endpoint(request: UserStoryRequest):
    return generate_code(request)
