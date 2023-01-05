DEFAULT_ZENKAKU_LEN = 2.08
def calculate_excel_width(column_datas,char_width=DEFAULT_ZENKAKU_LEN):
    max_len = 0
    for data in column_datas:
        for line in data.split("\n"):
            if len(line) >= max_len:
                max_len = len(line)
    
    return max_len * char_width
    