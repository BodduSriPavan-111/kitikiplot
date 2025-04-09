# Unit Test for Kitikiplot
==========================

This is a unit test file for the Kitikiplot project. It contains tests for the `KitikiPlot` class and its methods.

## Requirements

* Python 3.10 or later
* Pytest 8.3.5 or later

## Installation

To run the tests, follow these steps:

## Create a Virtual Environment

Create a new virtual environment using the following command:
```bash
python -m venv venv
```

## Activate the Virtual Environment

To activate the virtual environment, run the following command:

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

This will activate the virtual environment and you should see the name of the virtual environment printed on your command line.

## Install Dependencies

Once the virtual environment is activated, install the required dependencies by running:
```bash
pip install -r requirements.txt
```

## Running the Unit Tests

To run the Unit tests, navigate to the root directory of the project and run
```bash
pytest -s -vv tests/unit_test/unit_test.py
```
## Running the Unit Tests [Pytests] In CiCd pipeline
```import sys
sys.path.append('.')
```
As a Github Hosted Runner is Isolated at evry run .We have used Virtual Env For Python package Management. Pytests are Failed for Custom Packages ,So we can Initialze and run The tests By appending System path of test directory To Root Directory .Pytest will assume the kitikiplot as package and runs tests successfully

## Contributing

To contribute to this project, please submit a pull request with your changes. Make sure to include a description of the changes and any relevant test cases.

