# Overview

This repository is focused on **automated testing** using the **pytest** framework in Python, combined with **Allure** for detailed test reporting. It includes numerous examples of different testing techniques, from basic test setup and assertions to complex parameterized tests. Additionally, the repository follows the **Page Object Model (POM)** to facilitate maintainable web testing automation, using tools like Selenium.

The primary goal is to build an understanding of different aspects of test automation, including writing robust test cases, using fixtures, handling dependencies, creating parameterized tests, and generating interactive reports.

## Contents

### 1. **DemoFirstTest & DemoFirstTest1**
- **Page URL tests (`page_URLs.py`)**: Validates different page URLs and tests interactions with web elements.
- **Basic test cases (`test_find_elements.py`, `test_first_run.py`)**: Initial exploratory tests to get familiar with test execution in pytest.

### 2. **DemoPytest**
This folder contains a variety of different test scripts, showcasing several important pytest features and scenarios:

- **Assertion Tests**:
  - **Soft Assertions (`test_assertion_SOFT.py`)**: Shows how to use pytest to verify multiple conditions without stopping the test on the first failure.
  - **Hard Assertions (`test_assertion_hard.py`)**: Demonstrates the usual behavior where a test stops at the first failed assertion.

- **Fixtures and Test Management**:
  - **Test Fixtures (`test_fixtures_2.py`, `test_fixtures_mark2.py`)**: Uses pytest fixtures to set up preconditions required by multiple tests.
  - **Skipping Tests (`test_fixtures_skip.py`, `test_skip.py`)**: Example tests that are conditionally skipped using pytest’s skip markers.

- **Dependency and Failure Handling**:
  - **Dependencies (`test_dependency.py`)**: Demonstrates the use of pytest dependencies where certain tests depend on the outcome of previous tests.
  - **Handling Failures (`test_fail.py`, `test_stop.py`)**: Shows scenarios to handle failing tests or stop execution based on conditions.

- **Parameterized and Browser Tests**:
  - **Parameterized Tests (`test_parameters_headless.py`)**: Executes the same test with multiple inputs for thorough validation.
  - **Multi-browser Testing (`test_on_3_browsers.py`)**: Implements cross-browser testing for different environments (like Chrome, Firefox).

- **Group and Marker Tests**:
  - **Markers (`test_markers_group.py`)**: Groups related tests for better organization and runs them selectively based on certain criteria.
  - **Subset Tests (`test_multiple_subset_form.py`, `test_multiple_subset_iphone.py`)**: Uses different subsets of data to test specific cases, e.g., iPhone testing scenarios.

### 3. **Page Object Model (POM) Implementation (`pages`)**
Implements the **Page Object Model (POM)** to structure test scripts for better readability and easier maintenance:
- **Base Page (`base_page.py`)**: A common base class with reusable methods that all pages inherit.
- **Login Page (`login_page.py`)**: Contains locators and methods specific to the login page.
- **My Account Page (`my_account_page.py`)**: Handles interactions after logging in, like viewing or changing account details.
- **Change Password Page (`change_password_page.py`)**: Manages password change workflows.

### 4. **Utilities**
Contains various utility scripts to aid the testing process:
- **Test Configuration (`conftest.py`)**: Central configuration for pytest that defines fixtures used across multiple test files.
- **Fake Credentials (`fake_credentials.py`)**: Stores credentials and fake data used for testing purposes.
- **Main Script (`main.py`)**: Entry point for executing certain tests or functionalities.
- **Pytest Configuration (`pytest.ini`)**: Pytest-specific settings and options to streamline the testing process.

### 5. **RaportAllure**
Includes **Allure JSON files** (`*.json`) used to generate comprehensive test reports. These files are produced when tests are executed with the `--alluredir` option, allowing easy integration with Allure to create visual reports.

### 6. **Test Reports (`raport_testow.html`, `pytest_raport.html`)**
- HTML reports generated from pytest and Allure runs, which provide visual insights into test results, including passed, failed, or skipped tests, as well as statistical analysis of the test execution.

## Technologies Used

- **Python**: Core programming language used for all scripts and tests.
- **pytest**: A powerful testing framework that provides easy-to-write syntax, fixtures, and plugins for creating effective test suites.
- **Allure**: A flexible and detailed report generator that provides insightful visual feedback about the test runs.
- **Selenium** (optional): Used to interact with web pages for UI testing.
- **Page Object Model (POM)**: Design pattern that enhances the maintainability and readability of Selenium scripts by modeling web pages as classes.

## Purpose

This repository serves as a learning tool and practical exploration of different facets of test automation with **pytest**. The main focus areas include:

- **Writing Automated Tests**: 
  - Exploring different levels of assertions (soft vs. hard assertions) to manage various testing requirements.

- **Creating Reusable Test Setups**:
  - Utilizing pytest fixtures to create preconditions that can be reused across multiple test cases, making the test code more maintainable.

- **Managing Dependencies and Skipping Tests**:
  - Handling test dependencies and scenarios where tests need to be conditionally skipped, ensuring flexible test execution.

- **Cross-Browser and Parameterized Testing**:
  - Running the same tests across multiple browsers to verify compatibility, as well as using parameterized tests to validate different sets of input data efficiently.

- **Implementing the Page Object Model (POM)**:
  - Structuring test scripts using the **Page Object Model** to improve maintainability and readability, especially when interacting with web elements via **Selenium**.

- **Generating Detailed Reports with Allure**:
  - Creating comprehensive and interactive reports using **Allure**, providing insights into test performance, failures, and overall coverage, thus making it easier to analyze test results.

