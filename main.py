from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status, Path, File, UploadFile
from pydantic import BaseModel
import uvicorn
from models import File
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import os
from fastapi.responses import FileResponse
from datetime import datetime,date



app = FastAPI()

path = "/Users/Dell/Documents/Fastapi/Watch"

models.Base.metadata.create_all(bind= engine)

def get_db():
    try: 
       db = SessionLocal()
       yield db

    finally:
        db.close()
    
db_dependency = Annotated[Session, Depends(get_db)]

class FileRequest(BaseModel):
    date_ :date = datetime.now().date()
    filename : str 
    location : str


@app.get("/files/{file_name}")
async def read_file(file_name: str, db: db_dependency):
    file_path = os.path.join(path, "Files/Music.txt")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="text/html", filename="Music.txt")
    file_model = db.query(File).filter(File.filename == file_name).first()

    if file_model is not None:
        return file_model
    
    db.add(file_model)
    db.commit()

    raise HTTPException(status_code=404, detail='File not found')



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3316)


