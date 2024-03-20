from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with


driver = webdriver.Chrome()
driver.get("https://m-tsec.digitaledu.in/#/landingpage/login?regType=&regId=&regUserType=alumni&regTitle=&mobile=&authMethod=oma")
print(driver.title)

# enter your username and password
user_username = ""
user_password = ""

# enter login screen
login_button = ".mat-focus-indicator.login-button.mat-raised-button.mat-button-base.mat-primary.ng-star-inserted"
login = driver.find_element(By.CSS_SELECTOR, login_button)
# Wait for up to 10 seconds
welcome_screen = WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.ID, "welcome_screen")))
login.click()

# enter login info
login_uname_input = "mat-input-2"
login_password_input = "mat-input-3"

# username = driver.find_element(By.ID, login_uname_input)
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, login_uname_input))  # Or replace ID with another locator
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, login_password_input))  # Or replace ID with another locator
)

username.send_keys(user_username)
password.send_keys(user_password)

# submit login info
old_url = driver.current_url
submit_button = ".mat-focus-indicator.mat-raised-button.mat-button-base.mat-primary"
submit = driver.find_element(By.CSS_SELECTOR, submit_button)
submit.click()

# check if logged in
if EC.url_changes(old_url):
    print("Logged In")
else:
    print("Not logged in")
    
# click on account image
account_image_XPATH = '//*[@id="page_body"]/app-dashboard/mat-sidenav-container/mat-sidenav-content/mat-toolbar/span[3]/div[5]/img'
account_image = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, account_image_XPATH)))
account_image.click()

# get student name if logged in
student_name = ".user-name.dg-text-header-medium"
student_name_ = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, student_name))
)
print(student_name_.text)

# click out of account menu
click_after_account_menu_css = ".cdk-overlay-backdrop.cdk-overlay-transparent-backdrop.cdk-overlay-backdrop-showing"
click_after_account_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, click_after_account_menu_css)))
click_after_account_menu.click()

# navigate to assignment section
hamburger_icon_button_css = ".mat-focus-indicator.mat-icon-button.mat-button-base"
hamburger_icon_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, hamburger_icon_button_css)))
hamburger_icon_button.click()

# goto assignment section
assignment_page_button_css = ".flex:.1.1.calc(100% - 70px);.box-sizing:.border-box;.min-width:.calc(100% - 70px);"
assignment_page_button_XPATH = '//*[@id="page_body"]/app-dashboard/mat-sidenav-container/mat-sidenav/div/div[2]/div[6]/div[1][text()="assignment"]'
assignment_page_button_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mat-icon.notranslate.material-icons.mat-icon-no-color")))
print(assignment_page_button_icon.text)
div_right_of_assignment_page_button_icon = driver.find_element(locate_with(By.TAG_NAME, "div").to_right_of(assignment_page_button_icon))
assignment_page_div = driver.find_element(locate_with(By.TAG_NAME, "div").to_right_of(div_right_of_assignment_page_button_icon))
assignment_page_div.click()

# get assignment page header
assignment_page_header_XPATH = '//*[@id="page_body"]/app-dashboard/mat-sidenav-container/mat-sidenav-content/div/div/assignment/div[1]/dashboard-control-panel/div/div/mat-card/div/div[2]'
assignment_page_header_css = "dg-text-header-large"
assignment_page_header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, assignment_page_header_XPATH)))
print(assignment_page_header.text)

driver.quit()
