from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.ProdPage import ProdPage
from Pages.CartPage import  CartPage
from Pages.CheckoutPage import CheckoutPage
from Pages.CheckoutOverviewPage import CheckoutOverviewPage

def test_shop(browser):
    user = "standard_user"
    password = "secret_sauce"
    login_page = LoginPage(browser)
    login_page.login(user, password)

    prod_page = ProdPage(browser)
    prod_page.add_multiple_items (["Sauce Labs Backpack","Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"])
    prod_page.go_to_card_page()


    cart_page = CartPage(browser)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(browser)
    checkout_page.fill_checkout_form("Aleksei", "Fomin", "614094")


    checkout_overview_page = CheckoutOverviewPage(browser)
    checkout_overview_page.wait_for_loaded()
    total = checkout_overview_page.get_total_amount("58.29")  # Передаем ожидаемую сумму
    assert total == 58.29
