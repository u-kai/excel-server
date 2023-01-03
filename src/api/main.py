import sys
from typing import List, Optional

sys.path.append("../lib")


from excel_writer import ExcelWriter
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class WriteContents(BaseModel):
    filename: str
    sheet: Optional[str] = "Sheet1"
    contents: List[List[str]]
    start_cell: Optional[str] = "A1"


TEMPLATE_XLSX = "../lib/template.xlsx"


@app.post("/write-contents")
async def write_contents(contents: WriteContents):
    writer = ExcelWriter(TEMPLATE_XLSX)
    writer.write_block_cell(
        contents.sheet, contents.start_cell, contents.contents
    )
    writer.save(contents.filename)
    return {"message": f"{contents.filename} is writed success"}
