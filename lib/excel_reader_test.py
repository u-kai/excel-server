from excel_reader import ExcelReader


def test_read_test_xlsx():
    filepath = "test.xlsx"
    reader = ExcelReader()
    _ = reader.read_wb(filepath)
    sheet = reader.read_sheet(filepath,"Sheet1")
    assert sheet["A1"].value == "hello"
    