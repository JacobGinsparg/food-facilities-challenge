from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from food_facilities_challenge.routers.facilities import router as FacilitiesRouter

app = FastAPI()


app.include_router(FacilitiesRouter)


@app.get("/")
def root():
    return RedirectResponse("/docs")
