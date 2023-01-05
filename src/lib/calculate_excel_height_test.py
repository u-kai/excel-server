from src.lib.calculate_excel_height import (DEFAULT_CHAR_HEIGHT,
                                            calculate_excel_height)


def test_calculate_excel_height():
    row_datas = [
        "abcd"+"\n"+"efghijk",#two line
        "abcde",
        "abcdef",
        "a",
    ]
    char_height = 1.0
    assert calculate_excel_height(row_datas,char_height) == 2.0
    row_datas = [
        "abcd"+"\n"+"efghijk"+"\n"+"l",#two line
        "abcde",
        "abcdef",
        "a",
    ]
    char_height = 1.0
    assert calculate_excel_height(row_datas,char_height) == 3.0

def test_calculate_excel_height_use_default():
    row_datas = [
        "abcd"+"\n"+"efghijk",#two line
        "abcde",
        "abcdef",
        "a",
    ]
    assert calculate_excel_height(row_datas,) == 2 * DEFAULT_CHAR_HEIGHT