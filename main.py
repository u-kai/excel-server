import sys
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from src.lib.excel_reader import ExcelReader
from src.lib.excel_writer import ExcelWriter

app = FastAPI()


TEMPLATE_XLSX = "src/lib/template.xlsx"


class WriteContents(BaseModel):
    filename: str
    sheet: Optional[str] = "Sheet1"
    contents: List[List[str]]
    start_cell: Optional[str] = "A1"
    ajust_size: Optional[bool] = True


@app.post("/write-contents")
async def write_contents(contents: WriteContents):
    writer = ExcelWriter(TEMPLATE_XLSX)
    writer.write_block_cell(
        contents.sheet, contents.start_cell, contents.contents
    )
    if contents.ajust_size:
        writer.ajust_cell_size(contents.sheet,contents.start_cell,contents.contents)
    writer.save(contents.filename)
    return {"message": f"{contents.filename} is writed success"}


class WriteContentsFromTemplate(BaseModel):
    template:str
    filename: str 
    sheet: Optional[str] = "Sheet1"
    contents: List[List[str]]
    start_cell: Optional[str] = "A1"


@app.post("/from-template")
async def write_contents_from_template(contents:WriteContentsFromTemplate):
    writer = ExcelWriter(contents.template)
    writer.write_block_cell(contents.sheet,contents.start_cell,contents.contents)
    writer.save(contents.filename)
    return {"message":f"{contents.filename} is writed success"}


class ReadContents(BaseModel):
    filename:str
    sheet: Optional[str] = "Sheet1"
    cell:str

reader = ExcelReader()


@app.post("/read-cell")
async def read_cell(contents:ReadContents):
    cell = reader.read_cell(contents.filename,contents.sheet,contents.cell)
    if cell is None:
        return {"index":contents.cell,"value":""}

    return {"index":contents.cell,"value":cell}


class ReadCellsContents(BaseModel):
    filename:str
    sheet: Optional[str] = "Sheet1"
    start_cell:str
    end_cell:str

@app.post("/read-cells")
async def read_cells(contents:ReadCellsContents):
    cells = reader.read_block_cell(contents.filename,contents.sheet,contents.start_cell,contents.end_cell)

    return {"start":contents.start_cell,"end":contents.end_cell,"cells":cells}