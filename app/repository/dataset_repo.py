from app.db.schemas import Dataset
from sqlalchemy import exists

def create_dataset(db, dataset: Dataset):
    data = Dataset(
        name=dataset.name,
        file_path=dataset.file_path,
        type=dataset.type,
        real_dataset_id=dataset.real_dataset_id
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def get_dataset_by_id(db, dataset_id: int):
    return db.query(Dataset).filter(Dataset.id == dataset_id).first()

async def file_exists(db, filename: str) -> bool:
    return db.query(
        exists().where(Dataset.name == filename)
    ).scalar()