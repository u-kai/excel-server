from os import remove

from excel_reader import ExcelReader
from excel_writer import ExcelWriter


def test_excel_writer():
    write_file = "write-test.xlsx"
    writer = ExcelWriter("./lib/template.xlsx")
    writer.write_cell(write_file, "Sheet1", "A1", "hello")
    reader = ExcelReader()
    assert reader.read_cell("write-test.xlsx", "Sheet1", "A1") == "hello"
    remove(write_file)
    

def remove_file(filepath):
    remove(filepath)
