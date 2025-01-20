from fastapi import APIRouter
from app.models.design import DesignRequest, DesignResponse
from app.services.r2d import generate_design

router = APIRouter()

@router.post("/generate_design", response_model=DesignResponse)
async def generate_design_endpoint(request: DesignRequest):
    return generate_design(request)
