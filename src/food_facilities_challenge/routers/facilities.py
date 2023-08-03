from fastapi import APIRouter
from fastapi.responses import JSONResponse
from food_facilities_challenge.database import database as db

router = APIRouter(
    prefix="/facilities",
    tags=["facilities"],
    responses={404: {"description": "Facilities not found."}},
)


@router.get("/")
def facilities_root():
    return JSONResponse({"message": "Hello there."})


@router.get("/search/applicant/{applicant}")
def get_facilities_by_applicant(applicant: str, status: str = None):
    applicant_facilities = db.query_applicant(applicant=applicant, status=status)
    return JSONResponse(
        {
            "Count": len(applicant_facilities),
            "Facilities": applicant_facilities,
        }
    )
