class CellSizeCalculator:
    def __init__(self,char_width,char_height) -> None:
       self.char_width = char_width 
       self.char_height = char_height 

    def calculate_heights(self,table_data):
        result = []
        for row in table_data:
            result.append(calculate_excel_height(row,self.char_height))
        return result

    def calculate_widths(self,table_data):
        result = []
        reversed = reverse(table_data)
        print(reversed)
        for column in reversed:
            result.append(calculate_excel_width(column,self.char_width))
        return result




def reverse(table_data):
    result = []
    row_lengths = [len(row) for row in table_data]
    max_row_length = max(row_lengths)
    for i in range(max_row_length):
        tmp = []
        for row in table_data :
            if i >= len(row):
                continue
            tmp.append(row[i])
        result.append(tmp)
    return result

DEFAULT_CHAR_HEIGHT = 2.08
def calculate_excel_height(row_datas,char_height=DEFAULT_CHAR_HEIGHT):
    max_len = 0
    for data in row_datas:
        if max_len <= len(data.split("\n")):
            max_len = len(data.split("\n"))

    return max_len * char_height


DEFAULT_ZENKAKU_LEN = 2.08
def calculate_excel_width(column_datas,char_width=DEFAULT_ZENKAKU_LEN):
    max_len = 0
    for data in column_datas:
        for line in data.split("\n"):
            if len(line) >= max_len:
                max_len = len(line)
    
    return max_len * char_width