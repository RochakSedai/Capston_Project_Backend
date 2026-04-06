from fastapi import APIRouter, UploadFile, Depends, HTTPException, Form, File
from sqlalchemy.orm import Session
from typing import Optional
from app.db.session import get_db
from app.models.dataset import DatasetType, DatasetCreate
from app.repository import create_dataset, get_dataset_by_id, file_exists
from app.services.file_upload import save_file


router = APIRouter()

@router.post("/upload-file/")
async def create_upload_file(
    type: DatasetType = Form(...),
    real_dataset_id: Optional[int] = Form(None),
    file: UploadFile = File(...), 
    db: Session = Depends(get_db)
    ):
    print("HY")
    if type == DatasetType.SYNTHETIC:
        if not real_dataset_id:
             raise HTTPException(
                status_code=400,
                detail="Synthetic data must have real_dataset_id"
            )

        real_dataset = get_dataset_by_id(db, real_dataset_id)

        if not real_dataset or real_dataset.type.value != DatasetType.REAL:
            print("How")
            raise HTTPException(
                status_code=400,
                detail="Invalid real dataset id: must reference an existing real dataset"
            )
    # save file

    if await file_exists(db, file.filename):
        raise HTTPException(
            status_code=400,
            detail="A dataset with this name already exists. Please choose a different name."
        )
    
    file_path = await save_file(file)

    # saving in DB
    data =  DatasetCreate(
        name=file.filename,
        file_path=file_path,
        type=type,
        real_dataset_id=real_dataset_id
    )

    dataset  = create_dataset(db, data)

    
    return {
        "id": dataset.id,
        "name": dataset.name,
        "type": dataset.type,
        "file_path": dataset.file_path
    }

