# MLOps Lab 1 – Testing & CI with GitHub Actions

This lab sets up a Python project with unit tests (pytest and unittest) and automates them with GitHub Actions.

## Project Structure

    First_lab/
    ├── .github/workflows/
    │   ├── pytest_action.yml     # Runs pytest on every push to main
    │   └── unittest_action.yml   # Runs unittest on every push to main
    ├── data/                     # Placeholder for datasets
    ├── src/
    │   └── calculator.py         # Arithmetic functions (fun1–fun4)
    ├── test/
    │   ├── test_pytest.py        # Pytest tests, incl. parametrized test
    │   └── test_unittest.py      # Unittest tests
    ├── requirements.txt
    └── README.md

## Functions in calculator.py

- `fun1(x, y)` – returns x + y
- `fun2(x, y)` – returns x - y
- `fun3(x, y)` – returns x * y
- `fun4(x, y)` – returns fun1 + fun2 + fun3

## Run Locally

    python3 -m venv lab_01
    source lab_01/bin/activate
    pip install -r requirements.txt
    pytest
    python -m unittest test.test_unittest

## CI with GitHub Actions

Both workflows trigger on every push to `main`:

- **Testing with Pytest** – runs pytest, generates a JUnit XML report, and uploads it as the `test-results` artifact.
- **Python Unittests** – runs the unittest suite.

Results are visible under the Actions tab of this repository.
