"""
test subpage
"""

import pathlib

from fastapi import (
    APIRouter,
    Request,
)
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# templatesディレクトリの絶対パスを取得
PATH_TEMPLATES = str(
    pathlib.Path(__file__).resolve() \
        .parent.parent / "templates"
)
# Jinja2のobject生成
templates = Jinja2Templates(directory=PATH_TEMPLATES)


# サブアプリ
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def site_root(
    request: Request,
):
    """test subpage"""
    title = "test subpage"
    return templates.TemplateResponse(
        "subpage/index.html",   # `templates`ディレクトリにおける相対パス
        context={   # 変数をdict形式で渡すことが出来る
            "request": request,
            "title": title,
        }
    )
