# Stepik__Unit4_Page_Object
**Course name**: Automated testing with python and selenium

**Course link**: https://stepik.org/course/575

## Task descriptions
https://stepik.org/lesson/201964 step 1 to 14

## Tech
- Git
- Python 3.6 or later
- chromedriver
- geckodriver

## Prepare run on Windows

```sh
$ git clone https://github.com/Hanuky/Stepik__Unit4_Page_Object.git
$ cd stepik_575_unit4_po
$ python -m venv venv
$ venv/Scripts/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

## Run tests examples

```sh
# run only tests with need_review mark
$ pytest -v --tb=line --language=en -m need_review

# run all tests in test_main_page.py
$ pytest -v --tb=line --language=en test_main_page.py

# run all tests in test_product_page.py
$ pytest -v --tb=line --language=en test_product_page.py

# run all tests
$ pytest -v --tb=line --language=en
```

### Test run results example

![run_all_tests_result_screenshot](https://imgur.com/87dqJxe)