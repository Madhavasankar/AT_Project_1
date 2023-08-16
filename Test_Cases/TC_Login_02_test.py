import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCase2:

    def test_tc_login_02(self):
        """
        Checking the application is login functionality with invalid credentials
        :return: The invalid credentials message
        """
        _expected_error_msg = "Invalid credentials"  # actual error message
        actual_error_msg = HrmFunctionalities().login_to_hrm_incorrectly()  # getting the error msg of login page
        assert actual_error_msg == _expected_error_msg  # validating the actual error msg with _expected_error msg
        print(actual_error_msg)  # Printing the error message
