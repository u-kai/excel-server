

class ExcelIndex:
    def __init__(self,index:str):
        self.index = index 

    def value(self)->str:
        return self.index

    def right(self):
        return ExcelIndex("B1")


class AlfabetIndex:
    ALFABET_NUM = 26
    ALFABETS = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,}
    def __init__(self,alfabets):
        self.alfabets = alfabets


    def to_number(self):
        number = 0
        splited = list(self.alfabets)
        splited.reverse()
        for digit,alfabet in enumerate(splited):
            alfabet_num = AlfabetIndex.ALFABETS[alfabet]
            digit_effect = AlfabetIndex.ALFABET_NUM**digit
            this_digit_alfabet_num = alfabet_num * digit_effect
            number += this_digit_alfabet_num
        return number

    def value(self):
        return self.alfabets

    def next(self):
        return AlfabetIndex("B")