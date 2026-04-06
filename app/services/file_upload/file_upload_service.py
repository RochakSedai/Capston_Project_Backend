import os

UPLOAD_DIR = "data" 

os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_file(file):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return file_path