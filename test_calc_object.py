
from selenium import webdriver
from Pages.MainPage import MainPage





def test_calkulator(chrome_browser):
    time_ = 45
    main_page = MainPage(chrome_browser, delay=time_)

    main_page.set_delay()
    main_page.send_expression("7+8")
    main_page.click_equal()

    expected = "15"
    actual = main_page.get_result_text(expected=expected)
    assert actual.strip() == expected

