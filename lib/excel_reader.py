from openpyxl import load_workbook


class ExcelReader:
    def __init__(self) -> None:
        self.wb_cache = dict() 
        self.sheet_cache = dict() 
     
    def read_cell(self,filepath,sheet_name,cell_index):
        sheet = self.read_sheet(filepath,sheet_name)
        return sheet[cell_index].value

    def read_wb(self,filepath):
        if filepath in self.wb_cache:
            return self.wb_cache[filepath]

        wb = load_workbook(filepath)
        self.__cache_wb(filepath,wb)
        return wb
        
    def read_sheet(self,filepath,sheet_name):
        for key in self.wb_cache.keys():
            if key == filepath:
                sheet = self.wb_cache[key][sheet_name]
                self.__cache_sheet(filepath,sheet_name,sheet)
                return sheet

        wb = self.read_wb(filepath)
        self.__cache_wb(filepath,wb)
        sheet = self.wb_cache[filepath][sheet_name]
        self.__cache_sheet(filepath,sheet_name,sheet)
        return sheet
    
    def __cache_wb(self,filepath,wb):
        self.wb_cache.update({filepath:wb})
        return

    def __cache_sheet(self,filepath,sheet_name,sheet):
        entry = self.__make_cache_sheet_entry(filepath,sheet_name)
        self.sheet_cache.update({entry:sheet})
        return

    def __make_cache_sheet_entry(self,filepath,sheet_name):
        return filepath + sheet_name