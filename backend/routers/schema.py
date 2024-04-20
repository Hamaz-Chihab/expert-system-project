from pydantic import BaseModel
class ErrorResponse(BaseModel):
    error: str

class MyModel(BaseModel):
    class Config:
        from_attributes = True
class SymptomBase(BaseModel):
    description: str
    disease_id: int


class DiseaseBase(BaseModel):
    title: str
    description: str
    treatment: str


class UserSymptoms(BaseModel):
    symptom1: str
    symptom2: str
    symptom3: str


class SymptomDisplay(BaseModel):
    description: str

    class Config:
        orm_mode = True


class DiseaseDisplay(BaseModel):
    title: str
    description: str
    treatment: str

    class Config:
        orm_mode = True
