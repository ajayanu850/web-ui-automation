from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"


def test_logout(page: Page):

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

    page.locator("#react-burger-menu-btn").click()

    page.locator("#logout_sidebar_link").click()

    expect(
        page.locator('[data-test="login-button"]')
    ).to_be_visible()

    print("\nLogout successful")
