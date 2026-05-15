from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class EvaluationRunCreate(BaseModel):
    run_id: str
    run_name: str

    created_at_label: Optional[str] = None
    status: str = "completed"

    real_dataset_name: str
    synthetic_dataset_name: str

    overall_similarity_score: Optional[float] = None
    numerical_similarity_score: Optional[float] = None
    categorical_similarity_score: Optional[float] = None
    relationship_similarity_score: Optional[float] = None

    metrics_used: Optional[List[str]] = []

    config_json: Dict[str, Any]
    result_json: Dict[str, Any]