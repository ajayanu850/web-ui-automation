from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"


def test_valid_login(page: Page):

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

    print("\nLogin successful")

def test_invalid_login(page: Page):

    page.goto(BASE_URL)

    page.locator('[data-test="username"]').fill(
        "invalid_user"
    )

    page.locator('[data-test="password"]').fill(
        "wrong_password"
    )

    page.locator('[data-test="login-button"]').click()

    error_message = page.locator(
        '[data-test="error"]'
    )

    expect(error_message).to_be_visible()

    expect(error_message).to_contain_text(
        "Username and password do not match"
    )

    print("\nInvalid login validation successful")
