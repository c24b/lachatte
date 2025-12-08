#!/usr/bin/.venv/python

import json
from typing import Annotated
from enum import Enum, IntEnum
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional 

class Role(str, Enum):
    actif = "actif"
    passif = "passif"
    neutre = "neutre"


class Genre(str, Enum):
    homme = "H"
    femme = "F"

class KcalParameters(BaseModel):
    met: float = Field(3.5, gt=1, le=8)
    weight: int = Field(100, gt=20, lte=1000) #expressed in Kg
    duration: int = Field(60)  # expressed in minutes
    role: Role | None = "neutre"  # ponderation of MET by role or gender

app = FastAPI()

def load_json_data(fname):
    with open(fname, encoding="utf-8") as f:
        return json.load(f)

@app.get("/healthcheck")
def healthcheck():
    return {"status": 200, "message": "OK"}

@app.get("/positions")
def get_sexual_positions():
    return load_json_data("sexual_positions.json")
   
@app.get("/yoga")
def get_yoga_positions():
    return load_json_data("yoga_positions.json")

@app.get("/taichi")
def get_taichi_positions():
    return load_json_data("taichi_positions.json")

@app.get("/stretching")
def get_stretching_positions():
    return load_json_data("stretching_positions.json")

@app.get("/nutrition/")
def get_nutrition_facts():
    return load_json_data("nutrition_table.json")

@app.get("/kcal/")
def get_Kcal(filter_query: Annotated[KcalParameters, Query()]):
    met = float(getattr(filter_query, "met"))
    weight = int(getattr(filter_query, "weight"))
    duration = int(getattr(filter_query, "duration"))
    role = getattr(filter_query, "role", None)
    print(role)
    if role == "actif":
        met = float(met) * 1.1
    elif role == "passif":
        met = float(met) * 0.9
    else:
        role = "neutre"
    kcal = met * 3.5 * weight  * duration  / 200.0
    return {
        "met": met,
        "weight": weight,
        "duration": duration,
        "role": role,
        "kcal": kcal
        }


@app.get("/food/{kcal}")
def get_food_equivalent_of_kcal(kcal:float, max_results:int=3):
    nutrit = get_nutrition_facts()
    out = []
    for item in nutrit:
        kpp = item.get('kcal_per_portion')
        if not kpp:
            continue
        portions_needed = float(kcal) / float(kpp) if kpp else None
        match = round(portions_needed, 2)
        out.append({
            'aliment': item.get('aliment'),
            'ratio': match,
            'nearest': abs(round(1-match, 2))
        })
    best_equivalent = sorted(out, key= lambda x: x['nearest'])
    return best_equivalent[:max_results]

@app.get("/food_expense/")
def get_Kcal(filter_query: Annotated[KcalParameters, Query()]):
    met = float(getattr(filter_query, "met"))
    weight = int(getattr(filter_query, "weight"))
    duration = int(getattr(filter_query, "duration"))
    role = getattr(filter_query, "role", None)
    if role == "actif":
        met = float(met) * 1.1
    elif role == "passif":
        met = float(met) * 0.9
    else:
        role = "neutre"
    kcal = met * 3.5 * weight  * duration  / 200.0
    food_equivalent = get_food_equivalent_of_kcal(kcal)
    return {
        "met": met,
        "weight": weight,
        "duration": duration,
        "role": role,
        "kcal": kcal,
        "food_equivalent": food_equivalent
        }
