from sqlalchemy import Column, String, DateTime, Numeric, JSON, Integer, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from app.db.session import Base


class EvaluationRun(Base):
    __tablename__ = "evaluation_runs"

    run_id = Column(String(50), primary_key=True, index=True)
    run_name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    created_at_label = Column(String(50), nullable=True)
    status = Column(String(30), default="completed")

    real_dataset_id = Column(
        Integer,
        ForeignKey("datasets.id"),
        nullable=False
    )

    synthetic_dataset_id = Column(
        Integer,
        ForeignKey("datasets.id"),
        nullable=False
    )


    overall_similarity_score = Column(Numeric(5, 4), nullable=True)
    numerical_similarity_score = Column(Numeric(5, 4), nullable=True)
    categorical_similarity_score = Column(Numeric(5, 4), nullable=True)
    relationship_similarity_score = Column(Numeric(5, 4), nullable=True)

    metrics_used = Column(JSON, nullable=True)
    config_json = Column(JSON, nullable=False)
    result_json = Column(JSON, nullable=False)

    real_dataset = relationship(
        "Dataset",
        foreign_keys=[real_dataset_id]
    )

    synthetic_dataset = relationship(
        "Dataset",
        foreign_keys=[synthetic_dataset_id]
    )