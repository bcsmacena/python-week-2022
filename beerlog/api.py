from typing import List
from fastapi import FastAPI
from beerlog.core import get_beers_from_database, add_beer_to_database
from beerlog.serializers import BeerOut, BeerIn
from beerlog.database

api = FastAPI(title="Beerlog")

@api.get("/beers/", response_model=List[BeerOut])
def list_beers():
    beers = get_beers_from_database()
    return beers

@api.post("/beers/", response_model=BeerOut)
def add_beer(beer_in: BeerIn):
    beer = add_beer_to_database()