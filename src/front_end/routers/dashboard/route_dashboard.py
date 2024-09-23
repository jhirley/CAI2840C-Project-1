# from db.repository.jobs import list_jobs
# from db.repository.jobs import retreive_job
# from db.session import get_db
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
# from sqlalchemy.orm import Session

templates = Jinja2Templates(directory="src/front_end/templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
# async def home(request: Request, db: Session = Depends(get_db)):
async def home(request: Request):
    # jobs = list_jobs(db=db)
    return templates.TemplateResponse(
#         # "general_pages/dashboard.html", {"request": request, "jobs": jobs}
        "general_pages/dashboard.html", {"request": request}
    )

@router.get("/details/{id}")             #new
async def job_detail(id:int,request: Request):    
    # job = retreive_job(id=id, db=db)
    return templates.TemplateResponse(
        # "jobs/detail.html", {"request": request,"job":job}
        "jobs/detail.html", {"request": request}
    )

@router.get("/{full_path:path}")
async def catch_all(request: Request, full_path: str):
    return RedirectResponse(url="/")