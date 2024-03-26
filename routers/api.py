from fastapi import APIRouter, FastAPI, Depends, HTTPException
from starlette import status

from ice_breaker import ice_break


router = APIRouter()


@router.get("/query", status_code = status.HTTP_200_OK)
def checkUser(name: str):

    print("Hello Langchain")

    person_info = ice_break(name=name)

    return {
        "summary": person_info.summary,
        "facts": person_info.facts
    }



