from typing import List, Union

from db import models
from db.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schema, utils

router = APIRouter()


@router.post("/symptoms/", response_model=schema.SymptomDisplay)
def create_symptom(symptom: schema.SymptomBase, db: Session = Depends(get_db)):
    # Leverage Pydantic model for validation and data extraction
    db_symptom = models.Symptom(**symptom.dict())
    db.add(db_symptom)
    db.commit()
    db.refresh(db_symptom)

    # Create and return SymptomDisplay object
    symptom_display = schema.SymptomDisplay(
        id=db_symptom.id,
        description=db_symptom.description,
        disease_title=db_symptom.disease.title if db_symptom.disease else None,
    )
    return symptom_display


@router.post("/disease/", response_model=schema.DiseaseDisplay)
def create_desease(disease: schema.DiseaseBase, db: Session = Depends(get_db)):
    try:
        db_disease = models.Disease(**disease.dict())
        db.add(db_disease)
        db.commit()
        db.refresh(db_disease)

        # Create and return ProblemDisplay object
        disease_display = schema.DiseaseDisplay(
            id=db_disease.id,
            title=db_disease.title,
            description=db_disease.description,
            treatment=db_disease.treatment,
            symptoms=(
                [
                    schema.SymptomDisplay(
                        id=symptom.id,
                        description=symptom.description,
                    )
                    for symptom in db_disease.symptoms
                ]
                if db_disease.symptoms
                else None
            ),
        )
        return disease_display
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/diseases/", response_model=List[schema.DiseaseDisplay])
def get_all_diseases(db: Session = Depends(get_db)):
    diseases = db.query(models.Disease).all()
    return diseases


@router.get("/symptoms/", response_model=List[schema.SymptomDisplay])
def get_all_symptoms(db: Session = Depends(get_db)):
    symptoms = db.query(models.Symptom).all()
    return symptoms



@router.post("/diagnose", response_model=Union[schema.DiseaseDisplay, schema.ErrorResponse])
def diagnose_route(symptoms: schema.UserSymptoms, db: Session = Depends(get_db)):
    try:
        diagnosis = utils.diagnose(symptoms)
        print('this is the diagnosis from the route :',diagnosis)
        if not diagnosis:
            raise HTTPException(status_code=404, detail="Diagnosis not found")
        print('this id the diagnosis title ',diagnosis.title)
        diagnosis_title = str(diagnosis.title).replace('"', '')  # Remove double quotes
        try:
            disease = db.query(models.Disease).filter(models.Disease.title == diagnosis_title).first()
        except Exception as e:
            print(f"An error occurred: {e}")        
        print('this is the disease from the route :',disease)
        if disease is not None:
            return schema.DiseaseDisplay(
                title=disease.title,
                description=disease.description,
                treatment=disease.treatment
            )

        raise HTTPException(status_code=404, detail="Disease not found in the database")

    except Exception as e:
        return schema.ErrorResponse(error=str(e))