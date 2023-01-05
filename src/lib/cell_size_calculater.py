class CellSizeCalculator:
    def __init__(self,char_width,char_height) -> None:
       self.char_width = char_width 
       self.char_height = char_height 

    def calculate_heights(self,table_data):
        result = []
        for row in table_data:
            result.append(calculate_excel_height(row,self.char_height))
        return result

#    def calculate_widths(self,table_data):
#        result = []
#        for column_data in table_data :
#           result.append(calculate_excel_width(column_data,self.char_width))
#        return result


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