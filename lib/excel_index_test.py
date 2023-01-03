from excel_index import ExcelIndex


def test_excel_index():
    index = ExcelIndex("A1")
    assert index.value() =="A1"