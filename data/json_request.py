from pydantic import BaseModel


class ArbJsonRequest(BaseModel):
    payload: dict
