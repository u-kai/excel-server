from excel_index import AlfabetIndex, ExcelIndex, NumberIndex


def test_excel_index():
    index = ExcelIndex("A1")
    assert index.value() =="A1"

def test_under_index():
    index = ExcelIndex("A1")
    under = index.under()
    assert under.value() == "A2"
    assert under.under().value() == "A3"

def test_right_index():
    index = ExcelIndex("A1")
    right = index.right()
    assert right.value() == "B1"
    right_right = right.right()
    assert right_right.value() == "C1"
    
def test_extract_alfabet():
    assert ExcelIndex.extract_alfabet("AA1") == "AA"
    assert ExcelIndex.extract_alfabet("BB1") == "BB"
    assert ExcelIndex.extract_alfabet("ZZ1") == "ZZ"

def test_extract_number():
    assert ExcelIndex.extract_number("AA1") == 1
    assert ExcelIndex.extract_number("AA2") == 2
    assert ExcelIndex.extract_number("AA9") == 9


    
def test_number_index():
    one = NumberIndex(1)
    assert one.str_value() == "1"

def test_nextnumber_index():
    one = NumberIndex(1)
    assert one.next().str_value() == "2"

def test_alfabet_index():
    a = AlfabetIndex("A")
    assert a.value() == "A"
    b = AlfabetIndex("B")
    assert b.value() == "B"
    
    
def test_to_number():
    a = AlfabetIndex("A")
    assert a.to_number() == 1
    a = AlfabetIndex("B")
    assert a.to_number() == 2
    aa = AlfabetIndex("AA")
    assert aa.to_number() == 27
    aa = AlfabetIndex("AB")
    assert aa.to_number() == 28
    
def test_from_number():
    a = AlfabetIndex.from_number(1)
    assert a.value() == "A"
    a = AlfabetIndex.from_number(27)
    assert a.value() == "AA"

def test_next_alfabet():
    a = AlfabetIndex("A")
    assert a.next().value()  == "B"
    a = AlfabetIndex("AA")
    assert a.next().value()  == "AB"