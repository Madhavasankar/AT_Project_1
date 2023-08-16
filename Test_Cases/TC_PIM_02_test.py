import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCase4:

    def test_tc_pim_02(self):
        """
        This test case deals with updating the existing user in PIM Module.
        After employee details update successfully. printing the text of successful Updated message
        :return: It is returning the Successfully Updated message after employee details update.
        """
        _expected_successful_msg = "Successfully Updated"  # expected message
        success_text = HrmFunctionalities().modifying_user_details_in_pim()  # actual message
        assert success_text == _expected_successful_msg  # validating both actual and expected message is equal or not
        print(success_text)  # Printing the Successfully Updated message
