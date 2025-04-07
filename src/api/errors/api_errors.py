from pydantic import BaseModel


class APIErrorMessage(BaseModel):
    type: str
    message: str
