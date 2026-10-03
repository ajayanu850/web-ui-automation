from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"


def login(page: Page):

    page.goto(BASE_URL)

    page.locator('[data-test="username"]').fill(
        "standard_user"
    )

    page.locator('[data-test="password"]').fill(
        "secret_sauce"
    )

    page.locator('[data-test="login-button"]').click()

    expect(page.locator(".title")).to_have_text(
        "Products"
    )


def test_add_product_to_cart(page: Page):

    login(page)

    page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    cart_badge = page.locator(
        ".shopping_cart_badge"
    )

    expect(cart_badge).to_have_text("1")

    page.locator(
        ".shopping_cart_link"
    ).click()

    expect(page.locator(".title")).to_have_text(
        "Your Cart"
    )

    product_name = page.locator(
        ".inventory_item_name"
    )

    expect(product_name).to_have_text(
        "Sauce Labs Backpack"
    )

    print("\nProduct added to cart successfully")

def test_remove_product_from_cart(page: Page):

    login(page)

    page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    page.locator(
        ".shopping_cart_link"
    ).click()

    expect(page.locator(".title")).to_have_text(
        "Your Cart"
    )

    page.locator(
        '[data-test="remove-sauce-labs-backpack"]'
    ).click()

    product_name = page.locator(
        ".inventory_item_name"
    )

    expect(product_name).to_have_count(0)

    print("\nProduct removed from cart successfully")
