from fastapi import FastAPI, Request, Response, Query   # type: ignore

app = FastAPI()

@app.get("/")
def root(req: Request):
    msg = f"FastAPI is working - request URL:${req.url}"
    print(msg)
    return {"message": msg} 

