from openpyxl import load_workbook


class ExcelReader:
    def __init__(self) -> None:
        self.wb_cache = dict() 
        self.sheet_cache = dict() 
     
    def read_wb(self,filepath):
        wb = load_workbook(filepath)
        self.__cache_wb(filepath,wb)
        return wb
        
    def read_sheet(self,filepath,sheet_name):
        for key in self.wb_cache.keys():
            if key == filepath:
                entry = self.__make_cache_sheet_entry(filepath,sheet_name)
                sheet = self.wb_cache[key][sheet_name]
                self.sheet_cache.update({entry:sheet})
                return sheet

        wb = self.read_wb(filepath)
        self.__cache_wb(filepath,wb)
        sheet = self.wb_cache[key][sheet_name]
        self.sheet_cache.update({entry:sheet})
        return sheet
    
    def __cache_wb(self,filepath,wb):
        self.wb_cache.update({filepath:wb})
        return

    def __make_cache_sheet_entry(self,filepath,sheet_name):
        return filepath + sheet_name