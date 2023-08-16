import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCase5:

    def test_tc_pim_03(self):
        """
        This test case deals with deleting the existing user in PIM Module.
        After employee deletion successfully. printing the text of successful Deleted message
        :return: It is returning the Successfully Deleted message after employee deletion.
        """
        _expected_msg = "Successfully Deleted"  # expected msg
        deleted_text = HrmFunctionalities().deleting_user_in_pim()  # actual msg
        assert deleted_text == _expected_msg  # Validating both expected and actual msgs equal or  not
        print(deleted_text)  # print Successfully Deleted Msg
