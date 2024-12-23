# 🖐 OpenCart Automated Testing 

This is my assignment 2 about automated testing with Selenium. 

The website I am testing is OpenCart demo with the URL: https://demo.opencart.com 

## ⭐ SET UP ENVIRONMENT
1. Download and install Python from the [official website](https://www.python.org/downloads/)

2. [Installing OpenCart on localhost and XAMPP Server](https://www.youtube.com/watch?v=GftTTFm58d8)  for automated testing allows you to easily check the functionality of the store without affecting the production environment. It enables running automated tests in a controlled environment, ensuring that features work correctly.

![image](https://github.com/user-attachments/assets/b508fed7-770b-4b0a-a48c-022543ccedd3)

3. Open the terminal and run the following command to install the Selenium library

```bash
  pip install selenium
```

4. Download WebDriver on Chrome

Place the WebDriver in a directory included in your PATH environment variable or specify the path to the WebDriver in your code. 

5. Clone the project 

```bash
  git clone https://github.com/lehuyen1012/OpenCart-Automated-Testing.git

```
6. Run the test scripts  

```bash
  python -m pytest D:\myproject\test\automated-testing-opencart\tests\test_responsive.py

```
