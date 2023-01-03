from os import remove

from excel_reader import ExcelReader
from excel_writer import ExcelWriter


def test_excel_writer():
    write_file = "write-test.xlsx"
    writer = ExcelWriter("./lib/template.xlsx")
    writer.write_cell("Sheet1", "A1", "hello")
    writer.save(write_file)
    reader = ExcelReader()
    assert reader.read_cell("write-test.xlsx", "Sheet1", "A1") == "hello"
    remove(write_file)


def test_excel_writer_write_block():
    writer = ExcelWriter("./lib/template.xlsx")
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
    print(contents)
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
