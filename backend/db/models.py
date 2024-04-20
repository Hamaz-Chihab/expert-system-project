from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .database import Base

class Disease(Base):
    __tablename__ = "diseases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    treatment = Column(Text)

    symptoms = relationship("Symptom", back_populates="disease")

class Symptom(Base):
    __tablename__ = "symptoms"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    disease_id = Column(Integer, ForeignKey("diseases.id"))

    disease = relationship("Disease", back_populates="symptoms")
