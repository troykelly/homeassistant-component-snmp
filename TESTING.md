# Testing Instructions for the SNMP Component

This document provides instructions for running tests on the SNMP component in this repository.

## Prerequisites

- Python 3 (recommended version: 3.12 or later).
- pip installed.
- (Optional) A virtual environment for isolating dependencies.

Before running the tests, install the required dependencies by running:

    pip install -r requirements.txt

## Running the Tests

To execute all tests, simply navigate to the repository root in your terminal and run:

    pytest

This command will discover and run all tests located in the "tests/" directory.

## Running Tests in a Virtual Environment

It is recommended to use a virtual environment. To set one up, execute the following commands:

On macOS/Linux:
    
    python -m venv venv
    source venv/bin/activate

On Windows:

    python -m venv venv
    venv\Scripts\activate.bat

Then install the dependencies:

    pip install -r requirements.txt

And run the tests:

    pytest

## Additional Options

- For increased verbosity, run:

      pytest -v

- If you are using the provided devcontainer configuration, you can run the tests inside the container.

## Troubleshooting

- If you experience module import errors, ensure that the PYTHONPATH includes the repository root.
- Verify that all dependencies have been installed correctly.
- Run the tests from the repository root to ensure proper discovery of test modules.

## Contact

For any queries or issues, please contact Troy Kelly at troy@troykelly.com.

Happy testing!