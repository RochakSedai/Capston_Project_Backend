from pydantic import BaseModel
from typing import Optional
from enum import Enum

class DatasetType(str, Enum):
    REAL = "real"
    SYNTHETIC = "synthetic"

class DatasetCreate(BaseModel):
    name: str
    file_path: str
    type: DatasetType
    real_dataset_id: Optional[int] = None

class UploadDataset(BaseModel):
    type: DatasetType
    real_dataset_id: Optional[int] = None