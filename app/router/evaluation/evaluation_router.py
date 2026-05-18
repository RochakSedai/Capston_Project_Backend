# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.db.session import get_db

# from app.services.evaluation.evaluation_service import compute_similarity

# router = APIRouter()

# @router.post("/evaluate/")
# def evaluate(real_id: int, synthetic_id: int, db: Session = Depends(get_db)):
#     result = compute_similarity(db, real_id, synthetic_id)
#     return result
