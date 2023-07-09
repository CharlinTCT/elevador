from fastapi import FastAPI
import asyncio, time

LIST_FLOORS = []

app = FastAPI()

max_floor = 10


async def elevator(lista_de_pisos):
    lista_dentro = []
    lista_afuera = []
    for accion in lista_de_pisos:
        if accion["location"] == "inside":
            lista_dentro.append(accion)
        else:
            lista_afuera.append(accion)
    lista_de_pisos = lista_dentro + lista_afuera

    # await asyncio.sleep(20)

    lista_de_pisos.pop(0)

    return lista_de_pisos


@app.get("/list_floors")
def root():
    global LIST_FLOORS
    return {"floor_list": LIST_FLOORS}


@app.get("/call_elevator")
async def call_elevator(location: str, floor: int):
    if (floor > max_floor) or (floor < 0):
        return {"message": "The Build don't have this floor"}
    global LIST_FLOORS
    LIST_FLOORS.append({"location": location, "floor": floor})
    LIST_FLOORS = await elevator(LIST_FLOORS)
    return {"message": f"Call elevator from {location} on floor {floor}"}
