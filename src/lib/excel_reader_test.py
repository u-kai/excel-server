from src.lib.excel_reader import ExcelReader

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

def test_read_block_cell():
    reader = ExcelReader()
    start_index = HELLO_CELL
    end_index = WORLD_CELL 
    block_cell = reader.read_block_cell(TEST_FILE,TEST_SHEET,start_index,end_index)
    assert block_cell == [["hello","world"]]
    block_cell = reader.read_block_cell(TEST_FILE,TEST_SHEET,start_index,"C1")
    assert block_cell == [["hello","world",None]]