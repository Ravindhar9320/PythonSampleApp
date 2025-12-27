from fastapi import FastAPI
import uvicorn

app = FastAPI()   # <-- You forgot this part

@app.get("/")  # type: ignore 
def read_root():
    return "Welcome to python programing"

msg = "Hello World"
print(msg)

# Optional: run the server
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)