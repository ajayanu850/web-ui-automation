# Web UI Automation Framework

A Python-based web UI automation project using Playwright and Pytest.

This project demonstrates automated browser testing for login, invalid login, cart operations, and logout using a public demo e-commerce website.

## Problem

Manual browser testing can be repetitive and time-consuming.

UI automation helps validate:

- Login workflows
- Error messages
- Product interactions
- Cart functionality
- Navigation
- Logout behavior

## Solution

This project uses Python, Playwright, and Pytest to automate end-to-end browser test scenarios.

## Test Scenarios

### Valid Login

Validates:

- Username input
- Password input
- Login button
- Successful navigation to Products page

### Invalid Login

Validates:

- Invalid credentials
- Error message visibility
- Expected error text

### Add Product to Cart

Validates:

- Successful login
- Product add-to-cart action
- Cart badge count
- Cart navigation
- Product name in cart

### Remove Product from Cart

Validates:

- Product added to cart
- Product removal
- Cart item count after removal

### Logout

Validates:

- Successful login
- Menu navigation
- Logout action
- Return to login screen

## Technologies Used

- Python
- Playwright
- Pytest
- Browser Automation
- Git
- GitHub

## Project Structure

```text
web-ui-automation/
│
├── README.md
├── requirements.txt
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_logout.py
│
└── Screenshots/
    └── ui_test_results.png
```

## Installation

Clone the repository:

```bash
git clone https://github.com/ajayanu850/web-ui-automation.git
```

Move into the project:

```bash
cd web-ui-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Chromium:

```bash
python -m playwright install chromium
```

## Run Tests

Run all tests:

```bash
pytest -v -s
```

Run tests in visible browser mode:

```bash
pytest -v -s --headed
```

## Expected Result

```text
test_add_product_to_cart PASSED
test_remove_product_from_cart PASSED
test_valid_login PASSED
test_invalid_login PASSED
test_logout PASSED

5 passed
```

## Project Screenshot

![Web UI Automation Test Results](Screenshots/ui_test_results.png)

## Skills Demonstrated

- Browser automation
- Playwright locators
- Pytest automation
- Positive testing
- Negative testing
- UI validation
- Cart workflow automation
- Error-message validation
- Reusable test functions
- Git version control

## Demo Website

This project uses SauceDemo, a public website designed for testing and automation practice.
