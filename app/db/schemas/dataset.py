from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from app.db.session import Base
import enum

class DatasetType(enum.Enum):
    REAL = "real"
    SYNTHETIC = "synthetic"

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    file_path = Column(String(255), nullable=False)  
    type = Column(Enum(DatasetType), nullable=False)
    description = Column(String(255), nullable=True)
    real_dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=True)