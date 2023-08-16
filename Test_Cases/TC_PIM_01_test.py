import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCase3:

    def test_tc_pim_01(self):
        """
        This test case deals with creating the user in PIM Module. After employee addition. printing the text of
        successful Saved message
        :return: It is returning the Successfully saved message after employee addition
        """
        _expected_successful_msg = "Successfully Saved"  # expected msg
        success_text = HrmFunctionalities().creating_user_in_pim_module()  # getting actual msg
        assert success_text == _expected_successful_msg  # validating both are equal or not
        print(success_text)  # printing the successfully saved msg
