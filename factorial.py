from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{starting_number}")
async def factorial(starting_number: int):
    if starting_number == 0:
        return {"result": False}
    
    result = 1
    number = starting_number
    
    while number > 1:
        result *= number
        number -= 1
    
    return {"result": result}

