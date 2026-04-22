import pytest
from string_utils import StringUtils
@pytest.mark.positive
@pytest.mark.parametrize("text, res",[("пиво", "Пиво"), ("рыбA", "РыбA"),("Чипсы","Чипсы"),("   ","   "),("а","А"),(".","."),("привет мир", "Привет мир"),
    ("уже всё Ок.", "Уже всё Ок."),("0,33 это мало", "0,33 это мало"),("!!!", "!!!")])
def test_capitalize_positive(text, res):
    cap = StringUtils()
    result = cap.capitalize(text)
    assert result == res

@pytest.mark.negative
@pytest.mark.parametrize("text", [None, ([])])
def test_capitalize_negative(text):
    cap = StringUtils()
    with pytest.raises(AttributeError):
        cap.capitalize(text)


@pytest.mark.positive
@pytest.mark.parametrize("text, res",[("  пиво", "пиво"), ("рыба ", "рыба "),("  Чипсы ","Чипсы "),("   ",""),(" а","а"),(". ",". "),("привет  мир", "привет  мир"),
("Уже всё Ок .", "Уже всё Ок ."),(" 123 Ёлочка гори!", "123 Ёлочка гори!"),("! ! !", "! ! !")])
def test_trim_positive(text, res):

    string = StringUtils()
    result = string.trim(text)
    assert result == res

@pytest.mark.negative
@pytest.mark.parametrize("text", [None, []])
def test_trim_negative(text):
    string = StringUtils()
    with pytest.raises(AttributeError):
        string.trim(text)


@pytest.mark.positive
@pytest.mark.parametrize("text, symbol, expected",[("Skypro","k", True),("Небо","б", True),("123", "2", True),("Skypro", "z", False)])
def test_contains_positive(text, symbol, expected):
    unit = StringUtils()
    assert unit.contains(text, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("text, symbol, expected", [
    ("Skypro", "z", False),
    ("", "s", False),
])
def test_contains_negative(text, symbol, expected):
    unit = StringUtils()
    assert unit.contains(text, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("text, symbol", [
    (None, "s"),
])
def test_contains_negative(text, symbol):
    unit = StringUtils()
    with pytest.raises(AttributeError):
        unit.contains(None, "s")


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, res",[("Водка", "к", "Вода"), ("рыбкA","к", "рыбA"),("Чипсы","с","Чипы"),("123","2", "13"),("Skypro","pro",'Sky'),("!?%","?",'!%'),("привет мир"," ", "приветмир"),
    ("Уже всё Ок.","всё", "Уже  Ок.")])


def test_delete_symbol_positive(string, symbol, res):
    unit = StringUtils()
    result = unit.delete_symbol(string, symbol)
    assert result == res

@pytest.mark.negative
@pytest.mark.parametrize("text, symbol, expected", [
    ("Skypro", "z", False),
    ("", "s", False),
])
def test_contains_negative_logic(text, symbol, expected):
    unit = StringUtils()
    assert unit.contains(text, symbol) == expected


@pytest.mark.negative
def test_contains_none_case():
    unit = StringUtils()
    with pytest.raises(AttributeError):
        unit.contains(None, "s")
