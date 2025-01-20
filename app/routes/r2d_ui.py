from fastapi import APIRouter

router = APIRouter()

@router.get("/get_ui")
async def get_ui():
    return {"message": "UI integration for R2D"}
