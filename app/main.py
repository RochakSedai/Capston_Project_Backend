from fastapi import FastAPI
from app.router.file_upload import file_upload_router
from app.router.evaluation import evaluation_router
from app.db.session import SessionLocal



app = FastAPI()

@app.on_event("startup")
def startup():
    from app.db.session import engine, Base
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ DB connected")
    except Exception as e:
        print("❌ DB connection failed:", e)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(file_upload_router, prefix="/api/v1")
app.include_router(evaluation_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with Poetry!"}
