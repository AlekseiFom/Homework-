import pytest
import allure
from Calc_page import MainPage


@allure.feature("Калькулятор")
@allure.severity("critical")
@allure.title("Проверка математических операций в медленном калькуляторе")
@allure.description("Тест устанавливает задержку,"
                    " вводит выражение и"
                    " проверяет итоговый результат на экране")
@pytest.mark.parametrize("expression, expected_result, time_", [
    ("7+8", "15", 15),
    ("9-3", "6", 10),
    ("4*5", "20", 20),
    ("8/2", "4", 5),
])
def test_calculator(
        chrome_browser, expression, expected_result, time_) -> None:
    """
    Тест калькулятора.
    :param expression: str
    :param expected_result: str
    :param time_: int
    """
    with allure.step(
            "Открыть страницу калькулятора и инициализировать PageObject"):
        main_page = MainPage(chrome_browser, delay=time_)

    with allure.step(f"Установить задержку калькулятора в {time_} сек."):
        main_page.set_delay()

    with allure.step(f"Ввести математическое выражение: {expression}"):
        main_page.send_expression(expression)

    with allure.step("Нажать на кнопку '='"):
        main_page.click_equal()

    with allure.step(
        f"Проверить отображение результата: {expected_result}"
    ):
        actual = main_page.get_result_text(expected=expected_result)
        assert actual.strip() == expected_result, (
            f"Ждали {expected_result}, но получили {actual}"
        )
