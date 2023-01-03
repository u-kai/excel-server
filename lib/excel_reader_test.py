from excel_reader import ExcelReader

TEST_FILE =  "test.xlsx"
TEST_SHEET = "Sheet1"
HELLO_CELL = "A1"
WORLD_CELL = "B1"

def test_read_test_xlsx():
    reader = ExcelReader()
    _ = reader.read_wb(TEST_FILE)
    sheet = reader.read_sheet(TEST_FILE,TEST_SHEET)
    assert sheet[HELLO_CELL].value == "hello"
    
    
def test_read_cell():
    reader = ExcelReader()
    cell = reader.read_cell(TEST_FILE,TEST_SHEET,HELLO_CELL)
    assert cell == "hello"
    cell = reader.read_cell(TEST_FILE,TEST_SHEET,WORLD_CELL)
    assert cell == "world"