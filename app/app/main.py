"""
app main
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def site_root():
    """root"""
    return {"message": "Hello, WORLD!"}
