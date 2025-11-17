# model/FilePath.py
from pydantic import BaseModel

class FilePath(BaseModel):
    file_path: str
