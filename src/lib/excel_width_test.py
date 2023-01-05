def test_calcrate_excel_width():
    column_datas = [
        "abcd",
        "abcde",
        "abcdef",
        "g",
    ]
    char_width = 1.0
    #assert calcrate_excel_width(column_datas,char_width) == 6.0