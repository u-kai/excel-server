

class ExcelIndex:
    def __init__(self,index:str):
        self.alfabet_index = AlfabetIndex(ExcelIndex.extract_alfabet(index)) 
        self.number_index = NumberIndex(ExcelIndex.extract_number(index)) 

    def from_custom_indexs(alfabet_index,number_index):
        result = ExcelIndex("A1")
        result.alfabet_index = alfabet_index 
        result.number_index = number_index 
        return result

    def gen_range_cell_strs(self,to_index):
        result = []
        tmp_number_index = self.number_index
        tmp_alfabet_index = self.alfabet_index
        while tmp_number_index.value() != to_index.number_index.next().value():
            row = []
            while tmp_alfabet_index.value() != to_index.alfabet_index.next().value():
                index = ExcelIndex.from_custom_indexs(tmp_alfabet_index,tmp_number_index)
                row.append(index.value())
                tmp_alfabet_index = tmp_alfabet_index.next()
            result.append(row)
            tmp_number_index = tmp_number_index.next()
            tmp_alfabet_index = self.alfabet_index
        return result

    def gen_range_cells(self,to_index):
        result = []
        tmp_number_index = self.number_index
        tmp_alfabet_index = self.alfabet_index
        while tmp_number_index.value() != to_index.number_index.next().value():
            row = []
            while tmp_alfabet_index.value() != to_index.alfabet_index.next().value():
                index = ExcelIndex.from_custom_indexs(tmp_alfabet_index,tmp_number_index)
                row.append(index)
                tmp_alfabet_index = tmp_alfabet_index.next()
            result.append(row)
            tmp_number_index = tmp_number_index.next()
            tmp_alfabet_index = self.alfabet_index
        return result
            
    
    def value(self)->str:
        return self.alfabet_index.value() + self.number_index.str_value()

    def right(self):
        return ExcelIndex.from_custom_indexs(self.alfabet_index.next(),self.number_index)

    def under(self):
        return ExcelIndex.from_custom_indexs(self.alfabet_index,self.number_index.next())

    
    def extract_number(index): 
        result = ""
        for c in index:
            i = int(c.encode("utf-8").hex(),16)
            if i > 47 and i < 58:
                result += c
        return int(result)
    
    def extract_alfabet(index):
        result = ""
        for c in index:
            i = int(c.encode("utf-8").hex(),16)
            if i > 64 and i<100:
                result += c
        return result

class NumberIndex:
    def __init__(self,number):
        self.number = number
    
    def next(self):
        return NumberIndex(self.number+1)

    def value(self):
        return self.number

    def str_value(self):
        return str(self.number)

class AlfabetIndex:
    ALFABET_NUM = 26
    ALFABETS = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,}
    NUM_TO_ALFABETS = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}

    def __init__(self,alfabets):
        self.alfabets = alfabets

    def from_number(number):
        if AlfabetIndex.ALFABET_NUM >= number :
            return AlfabetIndex(AlfabetIndex.NUM_TO_ALFABETS[number])
        
        mod_remain = number
        mod_acc = ""
        while mod_remain > AlfabetIndex.ALFABET_NUM:
            mod = mod_remain % AlfabetIndex.ALFABET_NUM
            mod_acc = f"{AlfabetIndex.NUM_TO_ALFABETS[mod]}{mod_acc}"
            mod_remain //= AlfabetIndex.ALFABET_NUM

        mod = mod_remain % AlfabetIndex.ALFABET_NUM
        mod_acc = f"{AlfabetIndex.NUM_TO_ALFABETS[mod]}{mod_acc}"
        return AlfabetIndex(mod_acc)
        

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
        this_number = self.to_number()
        next_number = this_number + 1
        return AlfabetIndex.from_number(next_number)