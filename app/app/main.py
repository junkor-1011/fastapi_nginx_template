"""
app main
"""

import pathlib

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from .routers import subpage

# const
PATH_STATIC = str(pathlib.Path(__file__).resolve().parent / "static")


def create_app():
    """create app"""
    _app = FastAPI()

    _app.include_router(
        subpage.router,
        prefix="/subpage",
        tags=["subpage"],
        responses={404: {"description": "not found"}},
    )

    # static
    _app.mount(
        "/static",
        StaticFiles(directory=PATH_STATIC, html=False),
        name="static",
    )

    return _app


app = create_app()


@app.get('/')
async def redirect_subpage():
    """redirect webpage"""
    return RedirectResponse(
        "/subpage",
    )
