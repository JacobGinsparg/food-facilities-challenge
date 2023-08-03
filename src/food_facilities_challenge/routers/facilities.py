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


@router.get("/search/street/{street}")
def get_facilities_by_street(street: str):
    street_facilities = db.query_street(street=street)
    return JSONResponse(
        {
            "Count": len(street_facilities),
            "Facilities": street_facilities,
        }
    )


@router.get("/search/location/{lat}/{long}")
def get_nearby_facilities(lat: float, long: float, allow_non_approved: bool = False):
    nearby_facilities = db.query_near(
        lat=lat,
        long=long,
        allow_non_approved=allow_non_approved,
    )
    return JSONResponse(
        {
            "Count": len(nearby_facilities),
            "Facilities": nearby_facilities,
        }
    )
