DEFAULT_CHAR_HEIGHT = 2.08
def calculate_excel_height(row_datas,char_height=DEFAULT_CHAR_HEIGHT):
    max_len = 0
    for data in row_datas:
        if max_len <= len(data.split("\n")):
            max_len = len(data.split("\n"))

    return max_len * char_height
