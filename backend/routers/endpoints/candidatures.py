from typing import Any
from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from db.supabase import get_candidatures
from db import deps


router = APIRouter()
templates = Jinja2Templates(directory="routers/templates")
router.mount("/static", StaticFiles(directory=".\.\static"), name="static")


@router.get("/candidatures")
async def candidatures(current_user: dict = Depends(deps.get_current_user)) -> Any:
    return get_candidatures()
