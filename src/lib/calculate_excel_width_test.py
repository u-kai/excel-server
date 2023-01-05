from src.lib.calculate_excel_width import calculate_excel_width


def test_calculate_excel_width():
    column_datas = [
        "abcd",
        "abcde",
        "abcdef",
        "a",
    ]
    char_width = 1.0
    assert calculate_excel_width(column_datas,char_width) == 6.0
    column_datas = [
        "abcd",
        "abcde",
        "abcdef",
        "a",
        "abcdefg",
    ]
    char_width = 2.0
    assert calculate_excel_width(column_datas,char_width) == 14.0

def test_calculate_excel_width_case_multiline():

    column_datas = [
        "abcd"+"\n"+"efg",#tobe len 4
        "abcde",
        "abcdef",
        "a",
    ]
    char_width = 1.0
    assert calculate_excel_width(column_datas,char_width) == 6.0

    column_datas = [
        "abcd"+"\n"+"efghijk",#tobe len 7
        "abcde",
        "abcdef",
        "a",
    ]
    char_width = 1.0
    assert calculate_excel_width(column_datas,char_width) == 7.0

def test_calculate_excel_width_use_default_length2_08():

    column_datas = [
        "abcd"+"\n"+"efg",#tobe len 4
        "abcde",
        "abcdef",
        "a",
    ]
    assert calculate_excel_width(column_datas) == 6*2.08