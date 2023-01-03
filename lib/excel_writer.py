from openpyxl import load_workbook


class ExcelWriter:
    def __init__(self, template_sheet_path):
        self.wb = load_workbook(template_sheet_path)
        pass

    def write_cell(self, filepath, sheet_name, cell_index, content):
        sheet = self.wb[sheet_name]
        sheet[cell_index] = content
        self.wb.save(filepath)
        return
