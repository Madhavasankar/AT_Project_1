class LoginPageLocators:
    def __init__(self):
        pass

    username_ele_xpath = "//input[@placeholder='Username']"
    password_ele_name_tag = "password"
    login_btn_xpath = "//button[@type='submit']"
    alert_xpath = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"
    pim_xpath = "//a[@href='/web/index.php/pim/viewPimModule']"
    add_user_xpath = "//button[normalize-space()='Add']"
    first_name_xpath = "//input[@name='firstName']"
    middle_name_xpath = "//input[@name='middleName']"
    last_name_xpath = "//input[@name='lastName']"
    user_id_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input " \
                    "oxd-input--active']"
    create_login_details_xpath = "//p[text()='Create Login Details']/following-sibling::div"
    username_pim_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/div[" \
                         "1]/div[1]/div[1]/div[2]/input[1]"
    password_xpath = "(//input[@type='password'])[1]"
    confirm_password_xpath = "(//input[@type='password'])[2]"
    btn_xpath = "//button[@type='submit']"
    employee_id_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input " \
                        "oxd-input--active']"
    nickname_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[" \
                     "2]/input"
    driving_license_xpath = "//form[1]/div[2]/div[2]/div[1]/div[1]/div[2]/input[1]"
    date_format_xpath = "//*[@placeholder='yyyy-mm-dd']"
    license_expiry_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[" \
                           "2]/div/div[2]/div/div/input"
    dob_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[" \
                "2]/div/div/input"
    marital_status_xpath = "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//div[2]//div[" \
                           "1]//div[2]//div[1]//div[1]//div[1]"
    male_radio_btn_xpath = "//label[normalize-space()='Male']//span[@class='oxd-radio-input oxd-radio-input--active " \
                           "--label-right oxd-radio-input']"
    military_service_xpath = "//div[4]//div[1]//div[1]//div[1]//div[2]//input[1]"
    select_ele_xpath = "//div[@class='oxd-select-text oxd-select-text--active'][1]"
    smoker_xpath = "//label[normalize-space()='Yes']//span[@class='oxd-checkbox-input oxd-checkbox-input--active " \
                   "--label-right oxd-checkbox-input']"
    indian_ele_xpath = "//*[text()='Indian']"
    single_ele_xpath = "//*[text()='Single']"
    blood_grp_ele_xpath = "//*[text()='B+']"
    save_btn_xpath = "//button[@type='submit'][normalize-space()='Save']"
    all_emp_ids_xpath = "(//div[@class='oxd-table-body'])/div/div/div[2]/div[1]"
    all_emp_last_names = "(//div[@class='oxd-table-body'])/div/div/div[4]/div[1]"
    all_emp_edit_btns = "//div[@class='oxd-table-cell-actions']/button[2]"
    all_emp_delete_btns = "//div[@class='oxd-table-cell-actions']/button[1]"
    employee_list_xpath = "//*[text() = 'Employee List']"

    successful_msg_xpath = "//p[text()='Successfully Saved']"

    save_btn_for_updated_details = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button"
    updated_success_msg = "//p[text()='Successfully Updated']"
    delete_btn_xpath = "//button[normalize-space()='Yes, Delete']"
    deleted_msg_xpath = "//p[text()='Successfully Deleted']"

