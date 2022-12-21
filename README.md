# LAB - Class 2
## Project: Modules and Testing
## Author: Harper Foley
## Links and Resources

* [GitHub Repo](https://github.com/hfoley2013/math-series)

## Setup

* Create a local repository on your machine
* Create a virtual environment on your machine
  * `python3 -m venv .venv`
  * NOTE: Replace `python3` with specific version of Python you are using
* Activate the virtual environment
  * `source .venv/bin/activate`
* Install the following packages:
  * `pip install pytest`
  * `pip install pytest-watch`
* Clone down the repo onto your local machine
  * `https://github.com/hfoley2013/math-series.git`

### How to initialize/run your application (where applicable)

* We use `pytest-watch` to run our tests in this program
* You can activate `pytest-watch` by running that command in the terminal
  * Any failed tests will populate as red
  * Any passed tests will populate as green

## Tests
* We conducted the tests in this program using `pytest`
* The tests were set up to test various values in each of the three functions (fibonacci, lucas, and sum_series) to validate that they were returning the expected integer in their respective series.
* 11 tests total were conducted:
  * 4 for fibonacci
  * 6 for lucas
  * 1 for sum_series