import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to create and initialize the driver
def create_driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5173")
    return driver

# Fixture for setting up and tearing down the driver
@pytest.fixture(scope="module")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

# Helper function to click a button
def click_button(driver, button_text):
    button = driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
    button.click()

# Helper function to get input and result values
def get_input_and_result(driver):
    input_field = driver.find_element(By.CLASS_NAME, "text-4xl")
    result_field = driver.find_element(By.CLASS_NAME, "text-3xl")
    return input_field.text, result_field.text

# Helper function to log scenario in HTML report
def log_scenario(description, expected, actual, status):
    with open("report.html", "a") as report:
        report.write(f"<tr><td>{description}</td><td>{expected}</td><td>{actual}</td><td>{status}</td></tr>")

# Write HTML Header
def initialize_report():
    with open("report.html", "w") as report:
        report.write("<html><head><title>Calculator Test Report</title></head><body>")
        report.write("<h1>Calculator Test Report</h1>")
        report.write("<table border='1' style='width:100%; text-align:center; font-family:Arial; background-color:#f4f4f4'><tr><th>Scenario</th><th>Expected Result</th><th>Actual Result</th><th>Status</th></tr>")

# Close HTML Report
def finalize_report():
    with open("report.html", "a") as report:
        report.write("</table></body></html>")

@pytest.fixture(scope="module", autouse=True)
def report_setup_teardown():
    initialize_report()
    yield
    finalize_report()

# Test Case 1: Basic Addition
def test_addition(driver):
    description = "Basic Addition: 2 + 3"
    click_button(driver, "2")
    click_button(driver, "+")
    click_button(driver, "3")
    click_button(driver, "=")
    _, result_text = get_input_and_result(driver)
    status = "Pass" if result_text == "5" else "Fail"
    log_scenario(description, "5", result_text, status)
    assert result_text == "5"

# Test Case 2: Exponentiation (x²)
def test_exponentiation(driver):
    description = "Exponentiation: 3²"
    click_button(driver, "AC")
    click_button(driver, "3")
    click_button(driver, "x²")
    click_button(driver, "=")
    _, result_text = get_input_and_result(driver)
    status = "Pass" if result_text == "9" else "Fail"
    log_scenario(description, "9", result_text, status)
    assert result_text == "9"

# Test Case 3: Division by Zero
def test_division_by_zero(driver):
    description = "Division by Zero: 5 / 0"
    click_button(driver, "AC")
    click_button(driver, "5")
    click_button(driver, "/")
    click_button(driver, "0")
    click_button(driver, "=")
    _, result_text = get_input_and_result(driver)
    status = "Pass" if result_text == "Error" else "Fail"
    log_scenario(description, "Error", result_text, status)
    assert result_text == "Error"

# Test Case 4: Scientific Function (sin)
def test_scientific_function(driver):
    description = "Scientific Function: sin(0)"
    click_button(driver, "AC")
    click_button(driver, "sin")
    click_button(driver, "0")
    click_button(driver, ")")
    click_button(driver, "=")
    _, result_text = get_input_and_result(driver)
    status = "Pass" if result_text == "0" else "Fail"
    log_scenario(description, "0", result_text, status)
    assert result_text == "0"

# Test Case 5: Subtraction
def test_subtraction(driver):
    description = "Subtraction: 10 - 4"
    click_button(driver, "AC")
    click_button(driver, "1")
    click_button(driver, "0")
    click_button(driver, "-")
    click_button(driver, "4")
    click_button(driver, "=")
    _, result_text = get_input_and_result(driver)
    status = "Pass" if result_text == "6" else "Fail"
    log_scenario(description, "6", result_text, status)
    assert result_text == "6"

# Test Case 6: Multiplication
def test_multiplication(driver):
    description = "Multiplication: 7 * 6"
    click_button(driver, "AC")
    click_button(driver, "7")
    click_button(driver, "*")
    click_button(driver, "6")
    click_button(driver, "=")
    _, result_text = get_input_and_result(driver)
    status = "Pass" if result_text == "42" else "Fail"
    log_scenario(description, "42", result_text, status)
    assert result_text == "42"

# Test Case 7: Logarithm
def test_logarithm(driver):
    description = "Logarithm: log(100)"
    click_button(driver, "AC")
    click_button(driver, "log")
    click_button(driver, "1")
    click_button(driver, "0")
    click_button(driver, "0")
    click_button(driver, ")")
    click_button(driver, "=")
    _, result_text = get_input_and_result(driver)
    status = "Pass" if result_text == "2" else "Fail"
    log_scenario(description, "2", result_text, status)
    assert result_text == "2"

# Test Case 8: Square Root
def test_square_root(driver):
    description = "Square Root: √25"
    click_button(driver, "AC")
    click_button(driver, "√")
    click_button(driver, "2")
    click_button(driver, "5")
    click_button(driver, "=")
    _, result_text = get_input_and_result(driver)
    status = "Pass" if result_text == "5" else "Fail"
    log_scenario(description, "5", result_text, status)
    assert result_text == "5"

# Test Case 9: Percentage
def test_percentage(driver):
    description = "Percentage: 50 %"
    click_button(driver, "AC")
    click_button(driver, "5")
    click_button(driver, "0")
    click_button(driver, "%")
    click_button(driver, "=")
    _, result_text = get_input_and_result(driver)
    status = "Pass" if result_text == "0.5" else "Fail"
    log_scenario(description, "0.5", result_text, status)
    assert result_text == "0.5"

# Test Case 10: Tangent
def test_tangent(driver):
    description = "Tangent: tan(45)"
    click_button(driver, "AC")
    click_button(driver, "tan")
    click_button(driver, "4")
    click_button(driver, "5")
    click_button(driver, ")")
    click_button(driver, "=")
    _, result_text = get_input_and_result(driver)
    status = "Pass" if "1" in result_text else "Fail"
    log_scenario(description, "1", result_text, status)
    assert "1" in result_text
