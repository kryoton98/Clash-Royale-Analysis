from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db

router = APIRouter()

@router.post("/create")
async def create_group(request: dict, db: AsyncSession = Depends(get_db)):
    return {"group_id": 1, "name": request.get("name")}

@router.get("/{group_id}/dashboard")
async def get_group_dashboard(group_id: int, db: AsyncSession = Depends(get_db)):
    return {"group_id": group_id}
