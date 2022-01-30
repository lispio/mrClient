import requests

from .templates.mpGetTemplate import mpGetQuery


def getMyPantryInfo():
    print(f"mpLINNK {mpGetQuery.mpEcho.value}")
    results = requests.get(mpGetQuery.mpEcho.value)
    print(results.status_code)
    print(results.text)
    return {"message": results.text}

