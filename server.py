from aoc_2024 import solve_day_1, solve_day_2, solve_day_3
from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
import uvicorn
import sys

functions = {
    "2024": {
        "1": solve_day_1,
        "2": solve_day_2,
        "3": solve_day_3,
    }
}

app = FastAPI()

@app.post("/aoc/{year}/{day}")
async def solve_aoc(year: str, day: str, data: list[str]):
    if year not in functions or day not in functions.get(year, {}):
        return JSONResponse(status_code=404, content={"error": "Function not found"})
    
    try:
        # filter out trailing empty strings
        for i in range(len(data) - 1, -1, -1):
            if data[i] == "":
                data.pop(i)
            else:
                break


        result = functions[year][day](data)
        return JSONResponse(content={"part_1": result[0], "part_2": result[1]})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.get("/static/{file_path:path}")
async def static_files(file_path: str):
    return FileResponse(f"static/{file_path}")

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    
    uvicorn.run(app, host="0.0.0.0", port=port)