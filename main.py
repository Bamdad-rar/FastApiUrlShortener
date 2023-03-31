import hashlib
from typing import Annotated

from fastapi import Body, FastAPI, HTTPException, Response

app = FastAPI()


url_pool = dict()


@app.get("/all")
def root():
    """returns all shortened urls"""
    return url_pool


@app.post("/shorten/")
def shorten(url: Annotated[str, Body(embed=True)]):
    # the most usual way of shortening the url based on a search i did was, hashing it by either md5 or sha256 then use that (or part of it) as the shortened url
    for short_url, real_url in url_pool.items():
        if url == real_url:
            return short_url

    code = hashlib.sha256(url.encode()).hexdigest()[:7]
    url_pool[code] = url
    return code


@app.get("/{code}")
def resolve(code: str, response: Response):
    if real_url := url_pool.get(code):
        response.headers["Location"] = real_url
        response.status_code = 301
    else:
        raise HTTPException(status_code=404, detail="URL NOT FOUND")
