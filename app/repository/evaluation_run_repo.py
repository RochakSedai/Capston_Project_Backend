from app.db.schemas import EvaluationRun


def create_evaluation_run(db, evaluation_run):
    data = EvaluationRun(
        run_id=evaluation_run.run_id,
        run_name=evaluation_run.run_name,
        created_at_label=evaluation_run.created_at_label,
        status=evaluation_run.status,

        real_dataset_name=evaluation_run.real_dataset_name,
        synthetic_dataset_name=evaluation_run.synthetic_dataset_name,

        overall_similarity_score=evaluation_run.overall_similarity_score,
        numerical_similarity_score=evaluation_run.numerical_similarity_score,
        categorical_similarity_score=evaluation_run.categorical_similarity_score,
        relationship_similarity_score=evaluation_run.relationship_similarity_score,

        metrics_used=evaluation_run.metrics_used,

        config_json=evaluation_run.config_json,
        result_json=evaluation_run.result_json
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