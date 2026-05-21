from pydantic import BaseModel

class AnimalResponse(BaseModel):
    id: int
    name: str
    age: int
    adopted: bool
    health_status: str

    class Config:
        from_attributes = True