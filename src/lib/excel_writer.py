from openpyxl import load_workbook

from src.lib.cell_size_calculater import CellSizeCalculator
from src.lib.excel_index import ExcelIndex


class ExcelWriter:
    def __init__(self, template_sheet_path):
        self.wb = load_workbook(template_sheet_path)
        pass

    def ajust_cell_size(self,sheet_name,start_index,contents,char_width,char_height):
        calclator = CellSizeCalculator(char_width=char_width,char_height=char_height)
        # heights = calclator.calculate_heights()
        start_index = ExcelIndex(start_index)
        index = start_index
        widths = calclator.calculate_widths(contents)
        for width in widths:
            self.wb[sheet_name].column_dimensions[index.alfabet()].width = width
            index = index.right()

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
