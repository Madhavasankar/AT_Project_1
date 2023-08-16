from Test_Data import user_credentials
from Test_Locators.locators import LoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.select import Select


class HrmFunctionalities:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.my_wait = WebDriverWait(self.driver, 10)
        self.locators = LoginPageLocators
        self.url = user_credentials.url
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def login_to_hrm_correctly(self):
        """
        This function is for Logging into HRM with valid credentials
        :return: None
        """
        username_ele = self.my_wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.locators.username_ele_xpath)))  # getting user name Element
        username_ele.send_keys(user_credentials.user_name)  # giving input to the user
        password_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.NAME, self.locators.password_ele_name_tag)))  # locating the password
        password_ele.send_keys(user_credentials.right_password_for_login)  # input giving to the password Element
        login_btn_ele = self.my_wait.until(EC.element_to_be_clickable((By.XPATH, self.locators.login_btn_xpath)))
        login_btn_ele.click()  # clicking on login button
        # return self.driver.title

    def title_of_page(self):
        """
        Getting the title of the successful login page
        :return: title of the page
        """
        self.login_to_hrm_correctly()  # calling the function of login to the HRM portal
        return self.driver.title  # getting the title of the page

    def login_to_hrm_incorrectly(self):
        """
        This function is for Logging into HRM with invalid credentials
        :return: It is returning the error msg of invalid credentials
        """
        username_ele = self.my_wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.locators.username_ele_xpath)))  # getting username Element
        username_ele.send_keys(user_credentials.user_name)

        password_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.NAME, self.locators.password_ele_name_tag)))  # locating the password

        password_ele.send_keys(user_credentials.wrong_password_for_login)  # input giving to the password Element

        login_btn_ele = self.my_wait.until(EC.element_to_be_clickable((By.XPATH, self.locators.login_btn_xpath)))

        login_btn_ele.click()  # clicking on login button

        error_ele = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.alert_xpath)))

        return error_ele.text  # getting error text of invalid credentials

    def creating_user_in_pim_module(self):
        """
        This function is for creating a user in PIM Module. In available elements we are giving inputs to 6-7 elements.
        :return: It is returning the successful msg of user creation.
        """
        self.login_to_hrm_correctly()  # calling a log in function

        pim_element = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.pim_xpath)))
        pim_element.click()  # Clicking on PIM element

        add_btn = self.my_wait.until(EC.element_to_be_clickable((By.XPATH, self.locators.add_user_xpath)))
        add_btn.click()  # Clicking on Add user Element

        first_name_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.first_name_xpath)))  # getting first_name
        first_name_ele.send_keys(user_credentials.first_name)  # input giving to the first_name Element

        middle_name_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.middle_name_xpath)))
        middle_name_ele.send_keys(user_credentials.middle_name)  # giving input to the middle_name_element

        last_name_ele = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.last_name_xpath)))
        last_name_ele.send_keys(user_credentials.last_name)  # giving input to the last_name element

        employee_id_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.employee_id_xpath)))
        # employee_id_ele.click()
        employee_id_ele.clear()
        employee_id_ele.send_keys(user_credentials.employee_id)
        # sending extra numbers to id no for skipping the user_id valid error and for validation purpose

        create_login_details_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.create_login_details_xpath)))
        create_login_details_ele.click()  # Clicking on create login details button

        username_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.username_pim_xpath)))
        username_ele.send_keys(user_credentials.username_pim)  # giving input to the user_name element in pim

        password_ele = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.password_xpath)))
        password_ele.send_keys(user_credentials.password)  # giving input to the password element in pim

        confirm_password_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.confirm_password_xpath)))

        confirm_password_ele.send_keys(user_credentials.confirm_password)  # input to confirm password element in pim

        btn_ele = self.driver.find_element(By.XPATH, self.locators.btn_xpath)
        btn_ele.click()  # clicking on save button

        nickname_ele = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.nickname_xpath)))
        nickname_ele.send_keys(user_credentials.nick_name)  # input giving to the nick_name element in pim

        driving_license_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.driving_license_xpath)))
        driving_license_ele.send_keys(user_credentials.driving_license_no)  # input to driving license no field

        license_expiry_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.license_expiry_xpath)))

        """
        getting the date format elements in pim module i.e., license validity date and date of birth ..
        """

        license_expiry_ele.send_keys(user_credentials.license_expiry_date)
        """
        Clicking first date format element i.e., license expiry date and giving input to the license expiry date field
        """

        dob_ele = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.dob_xpath)))
        dob_ele.send_keys(user_credentials.date_of_birth)

        """
        Clicking first date format element i.e., date of birth and giving input to the date of birth field
        """

        select_option_elements = self.my_wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, self.locators.select_ele_xpath)))

        select_option_elements[0].click()  # Clicking on the nationality Element

        ind_ele = self.my_wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.locators.indian_ele_xpath)))  # finding for the Indian element in dropdown
        ind_ele.click()  # Clicking on indian element

        select_option_elements[1].click()  # Clicking on the marital status Element

        marital_status_ele = self.my_wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.locators.single_ele_xpath)))  # Finding for the Single element
        marital_status_ele.click()  # Clicking on single element

        male_radio_btn_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.male_radio_btn_xpath)))
        male_radio_btn_ele.click()  # Clicking on radio button of Male

        military_service_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.military_service_xpath)))
        military_service_ele.send_keys(user_credentials.military_service)

        """
        giving input to the military service field element ex: 5 years
        """

        smoker_ele = self.my_wait.until(EC.element_to_be_clickable((By.XPATH, self.locators.smoker_xpath)))
        smoker_ele.click()  # Clicking on smoker element

        save_btns = self.my_wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.locators.save_btn_xpath)))

        """
        Getting two buttons on same xpath. One button for saving personal details and one button saving for blood group
        """

        save_btns[0].click()  # Clicking on personal details save button

        select_option_elements[2].click()  # Clicking on blood group dropdown which is already located

        bld_group = self.my_wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.locators.blood_grp_ele_xpath)))
        bld_group.click()  # Clicking on B+ blood group button

        save_btns[1].click()  # Clicking on blood group saving button

        success_msg_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.successful_msg_xpath)))

        return success_msg_ele.text  # returning the success msg from success msg element

    def modifying_user_details_in_pim(self):
        """
        Editing the 2 details  of a user which existing in employee table
        :return: it is returning the Successfully modified message
        """

        self.login_to_hrm_correctly()  # Calling the login function

        pim_element = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.pim_xpath)))
        pim_element.click()  # Clicking in PIM element

        employee_list_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.employee_list_xpath)))
        employee_list_ele.click()  # Clicking on employee List Element in PIM page

        all_emp_ids = self.my_wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.all_emp_ids_xpath)))
        count_of_all_users = len(all_emp_ids)  # Count of all users

        all_emp_last_names = self.my_wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.all_emp_last_names)))

        all_emp_edit_btns = self.my_wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.all_emp_edit_btns)))

        for i in range(0, count_of_all_users):  # by using the for loop extracting data of every user data
            employee_id = all_emp_ids[i].text  # getting emp id ele
            employee_last_name = all_emp_last_names[i].text
            emp_no = employee_id[4:]  # by using indexing accessing the emp id which we have sent while creating a user
            edit_ele = all_emp_edit_btns[i]  # getting edit ele
            #
            if emp_no == user_credentials.employee_id and employee_last_name == user_credentials.last_name:
                # Comparing the values of the table and values sent while creating a user
                edit_ele.click()  # if both are same clicking on edit element

                nickname_ele1 = self.my_wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.locators.nickname_xpath)))
                nickname_ele1.clear()
                nickname_ele1.send_keys(user_credentials.updated_nick_name)  # sending a nick_name value

                military_service_ele1 = self.my_wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.locators.military_service_xpath)))
                military_service_ele1.click()
                military_service_ele1.clear()

                military_service_ele1.send_keys(user_credentials.military_service)  # sending a military ele value

                save_btn1 = self.my_wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.locators.save_btn_for_updated_details)))

                save_btn1.click()  # Clicking on save btn.

                success_msg = self.my_wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.locators.updated_success_msg)))

                success_text = success_msg.text  # getting return text from success element
                return success_text  # returning the success_text

    def deleting_user_in_pim(self):

        """
        Deleting a user from employee list
        :return: It is returning the Successfully deletion message
        """
        self.login_to_hrm_correctly()  # Calling the login function

        pim_element = self.my_wait.until(EC.visibility_of_element_located((By.XPATH, self.locators.pim_xpath)))
        pim_element.click()  # Clicking on PIM element

        employee_list_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.employee_list_xpath)))
        employee_list_ele.click()  # Clicking on employee list element

        all_emp_ids = self.my_wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.all_emp_ids_xpath)))
        count_of_all_users = len(all_emp_ids)  # Count of all users

        all_emp_last_names = self.my_wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.all_emp_last_names)))

        all_emp_delete_btns = self.my_wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, self.locators.all_emp_delete_btns)))

        for i in range(0, count_of_all_users):

            employee_id = all_emp_ids[i]

            no = employee_id.text  # getting the text from employee id
            emp_no1 = no[4:]  # by using indexing accessing the emp id which we have sent while creating a user

            last_name_ele = all_emp_last_names[i]
            last_name1 = last_name_ele.text  # Getting the text of a last_name element

            delete_ele = all_emp_delete_btns[i]  # delete icon ele

            if emp_no1 == user_credentials.employee_id and last_name1 == user_credentials.last_name:
                delete_ele.click()  # Clicking on delete icon

                delete_yes_btn = self.my_wait.until(
                    EC.element_to_be_clickable((By.XPATH, self.locators.delete_btn_xpath)))

                delete_yes_btn.click()  # Clicking on Yes, Delete option

                delete_msg_ele = self.my_wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.locators.deleted_msg_xpath)))

                delete_text = delete_msg_ele.text  # getting text from deletion message
                return delete_text  # returning the deletion text


# obj = HrmFunctionalities()
# obj.title_of_page()
# obj.login_to_hrm_incorrectly()
# obj.creating_user_in_pim_module()
# obj.modifying_user_details_in_pim()
# obj.deleting_user_in_pim()
