from fastapi import FastAPI

app = FastAPI()


dict_of_urls = dict()


@app.get("/all")
def root():
    """ returns all shortened urls """
    return dict_of_urls


@app.post("/shorten")
def shorten():
    # shorten the url based on some logic...
    # return the shortened version
    # save the key, pair value for later retrieval / usage
    shortened_version = "something here"
    return shortened_version


@app.get("/{shortened_url}")
def resolve():
    # get the real url of the shortened url
    # redirect page to the real url
    pass