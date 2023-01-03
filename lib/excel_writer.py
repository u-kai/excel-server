from excel_index import ExcelIndex
from openpyxl import load_workbook


class ExcelWriter:
    def __init__(self, template_sheet_path):
        self.wb = load_workbook(template_sheet_path)
        pass

    def write_block_cell(self, sheet_name, start_index, contents):
        start_index = ExcelIndex(start_index)
        index = start_index
        for row in contents:
            for content in row:
                self.write_cell(sheet_name, index.value(), content) 
                index = index.right()
            start_index = start_index.under()  
            index = start_index

    def write_cell(self, sheet_name, cell_index, content):
        sheet = self.wb[sheet_name]
        sheet[cell_index] = content
        return

    def save(self, filepath):
        self.wb.save(filepath)
