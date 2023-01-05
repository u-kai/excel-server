from src.lib.cell_size_calculater import CellSizeCalculator


def test_cell_size_calculater():
    char_width = 1.0
    char_height = 1.0
    
    calculater = CellSizeCalculator(char_width,char_height)
    
    datas = [
        ["A"+"\n"+"Z","BC","DEF"],
        ["ABC","DEFG","HIJKL"+"\n"+"MN"+"\n"+"OPQR"],
    ]
    heights = calculater.calculate_heights(datas)
    assert heights == [2*char_height,3*char_height]
    
#    widths= calculater.calculate_widths(datas)
#    assert widths == [3*char_width,4*char_width,5*char_width]