from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.repository.evaluation_run_repo import save_evaluation_run, get_all_evaluation_runs, get_evaluation_run_by_id
from app.models import EvaluationRunRequest

router = APIRouter()

@router.post("/evaluation-run/save/")
def save_comparision(evaluation_run: EvaluationRunRequest, db: Session = Depends(get_db)):
    saved_data =  save_evaluation_run(db, evaluation_run)

    return {
        "id": saved_data.run_id,
        "run_name": saved_data.run_name,
        "created_at": saved_data.created_at,
        "created_at_label": saved_data.created_at_label,

        "real_dataset_id": saved_data.real_dataset_id,
        "synthetic_dataset_id": saved_data.synthetic_dataset_id,

        "overall_similarity_score": saved_data.overall_similarity_score,

        "metrics_used": saved_data.metrics_used,

        "status": saved_data.status
    }


@router.get("/evaluation-run/")
def list_comparisons(
    db: Session = Depends(get_db)
):
    comparisons = get_all_evaluation_runs(db)

    return [
        {
            "id": item.run_id,
            "run_name": item.run_name,
            "created_at": item.created_at,
            "created_at_label": item.created_at_label,

            "real_dataset_id": item.real_dataset_id,
            "synthetic_dataset_id": item.synthetic_dataset_id,

            "overall_similarity_score": item.overall_similarity_score,

            "metrics_used": item.metrics_used,

            "status": item.status
        }
        for item in comparisons
    ]

@router.get("/evaluation-run/{run_id}")
def get_saved_run(
    run_id: str,
    db: Session = Depends(get_db)
):
    evaluation_run = get_evaluation_run_by_id(db, run_id)

    if not evaluation_run:
        raise HTTPException(
            status_code=404,
            detail="Evaluation run not found"
        )

    return evaluation_run