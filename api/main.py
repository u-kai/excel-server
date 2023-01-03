from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class WriteContents(BaseModel):
    filename: str
    sheet: Optional[str] = "Sheet1"
    contents: List[List[str]]
    start_cell: Optional[str] = "A1"

@app.post("/write-contents")
async def write_contents(contents:WriteContents):
    return {"message": contents.filename}
