from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict, Any


class EvaluationRunRequest(BaseModel):
    evaluationConfig: Dict[str, Any]
    evaluationResult: Dict[str, Any]
    realDatasetId: int
    syntheticDatasetId: int
    metricsUsed: List[str]

class EvaluationRunResponse(BaseModel):
    id: str
    run_name: str
    created_at: datetime
    created_at_label: str
    real_dataset_id: int
    synthetic_dataset_id: int
    overall_similarity_score: float | None
    metrics_used: List[str]
    status: str
