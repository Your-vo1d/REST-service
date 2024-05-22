from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    secret_code: str
    salary: float
    promotion_date: str