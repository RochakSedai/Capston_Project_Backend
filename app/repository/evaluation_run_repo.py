from uuid import uuid4
from datetime import datetime

from app.db.schemas import EvaluationRun
from app.models import EvaluationRunRequest
from .dataset_repo import get_dataset_by_id


def save_evaluation_run(db, evaluation_run: EvaluationRunRequest):
    run_id = f"run-{uuid4().hex[:8]}"
    synthetic_dataset_name = get_dataset_by_id(db, evaluation_run.syntheticDatasetId).name
    
    data = EvaluationRun(
        run_id=run_id,
        run_name=synthetic_dataset_name + "_evaluation",
        created_at_label=datetime.utcnow().strftime(
            "%d %b %Y %H:%M"
        ),
        status="completed",

        real_dataset_id=evaluation_run.realDatasetId,
        synthetic_dataset_id=evaluation_run.syntheticDatasetId,

        overall_similarity_score=evaluation_run.evaluationResult.get("overallSimilarityScore"),
        numerical_similarity_score=evaluation_run.evaluationResult.get("numericalSimilarityScore"),
        categorical_similarity_score=evaluation_run.evaluationResult.get("categoricalSimilarityScore"),
        relationship_similarity_score=evaluation_run.evaluationResult.get("relationshipSimilarityScore"),

        metrics_used=evaluation_run.metricsUsed,

        config_json=evaluation_run.evaluationConfig,
        result_json=evaluation_run.evaluationResult
    )

    db.add(data)
    db.commit()
    db.refresh(data)

    return data


def get_evaluation_run_by_id(db, run_id: str):
    return (
        db.query(EvaluationRun)
        .filter(EvaluationRun.run_id == run_id)
        .first()
    )


def get_all_evaluation_runs(db):
    return (
        db.query(EvaluationRun)
        .order_by(EvaluationRun.created_at.desc())
        .all()
    )


def delete_evaluation_run(db, run_id: str):
    run = (
        db.query(EvaluationRun)
        .filter(EvaluationRun.run_id == run_id)
        .first()
    )

    if run:
        db.delete(run)
        db.commit()

    return run