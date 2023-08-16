import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCases1:

    def test_tc_login_01(self):
        """
        Checking the application is correctly login or not with valid credentials and validating the title of
        the page after login.
        :return: The User successfully logged in message
        """
        _expected_title = "OrangeHRM"  # actual title of the page after login to OrangeHRM
        actual_title = HrmFunctionalities().title_of_page()  # getting title from Login functionality
        assert actual_title == _expected_title  # validating the of the page with _expected_title
        print("The user is logged in successfully")  # returning the successful message
