from os import remove

from src.lib.excel_reader import ExcelReader
from src.lib.excel_writer import ExcelWriter


def test_excel_writer():
    write_file = "write-test.xlsx"
    writer = ExcelWriter("./src/lib/template.xlsx")
    writer.write_cell("Sheet1", "A1", "hello")
    writer.save(write_file)
    reader = ExcelReader()
    assert reader.read_cell("write-test.xlsx", "Sheet1", "A1") == "hello"
    remove(write_file)

def test_excel_writer_ajust_cell_size():
    write_file = "write-test.xlsx"
    writer = ExcelWriter("./src/lib/template.xlsx")
    write_content = [
        [
            "A", "B", "C"
        ],
        [
            "DE", "FGH", "JKLM", "OPQRS"+"\n"+"U"
        ],
    ]
    sheet_name = "Sheet1"
    start_index = "A1"
    writer.ajust_cell_size(sheet_name,start_index,write_content,char_width=1.0,char_height=1.0)

    assert writer.wb[sheet_name].column_dimensions["A"].width == 2.0
    assert writer.wb[sheet_name].column_dimensions["B"].width == 3.0
    assert writer.wb[sheet_name].column_dimensions["C"].width == 4.0
    assert writer.wb[sheet_name].column_dimensions["D"].width == 5.0


def test_excel_writer_write_block():
    writer = ExcelWriter("./src/lib/template.xlsx")
    write_content = [
        [
            "A", "B", "C"
        ],
        [
            "D", "E", "F", "G"
        ],
        [
            "H", "I", "J", "K", "L"
        ],
    ]
    writer.write_block_cell("Sheet1", "A1", write_content)
    write_file = "write-test.xlsx"
    writer.save(write_file)
    reader = ExcelReader()
    contents = reader.read_block_cell("write-test.xlsx", "Sheet1", "A1", "E3")
    assert contents == [
        [
            "A", "B", "C", None, None
        ],

        [
            "D", "E", "F", "G", None
        ],

        [
            "H", "I", "J", "K", "L"
        ],
    ]

    remove(write_file)


def remove_file(filepath):
    remove(filepath)
