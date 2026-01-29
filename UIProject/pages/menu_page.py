from selenium.webdriver.common.by import By
from UIProject.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class MenuPage(BasePage):
    ADMIN_MENU = (By.XPATH, "//a[span[text()='Admin']]")
    PIM_MENU = (By.XPATH, "//a[span[text()='PIM']]")
    LEAVE_MENU = (By.XPATH, "//a[span[text()='Leave']]")
    TIME_MENU = (By.XPATH, "//a[span[text()='Time']]") 
    RECRUITMENT_MENU = (By.XPATH, "//a[span[text()='Recruitment']]")
    MYINFO_MENU = (By.XPATH, "//a[span[text()='My Info']]")
    PERFORMANCE_MENU = (By.XPATH, "//a[span[text()='Performance']]")
    DASHBOARD_MENU = (By.XPATH, "//a[span[text()='Dashboard']]")
    DIRECTORY_MENU = (By.XPATH, "//a[span[text()='Directory']]")
    MAINTENANCE_MENU = (By.XPATH, "//a[span[text()='Maintenance']]")
    CLAIM_MENU = (By.XPATH, "//a[span[text()='Claim']]")
    def click_admin(self):
        self.click(self.ADMIN_MENU, "Admin menu")
    def click_leave(self):
        self.click(self.LEAVE_MENU, "Leave menu")
    def click_pim(self):
        self.click(self.PIM_MENU, "PIM menu")
    def click_time(self):
        self.click(self.TIME_MENU, "Time menu")
    def click_recruitment(self):
        self.click(self.RECRUITMENT_MENU, "Recruitment menu")
    def click_myinfo(self):
        self.click(self.MYINFO_MENU, "My Info menu")
    def click_performance(self):
        self.click(self.PERFORMANCE_MENU, "Performance menu")
    def click_dashboard(self):
        self.click(self.DASHBOARD_MENU, "Dashboard menu")
    def click_directory(self):
        self.click(self.DIRECTORY_MENU, "Directory menu")
    def click_maintenance(self):
        self.click(self.MAINTENANCE_MENU, "Maintenance menu")
    def click_claim(self):
        self.click(self.CLAIM_MENU, "Claim menu")
    # One XPath to check PIM menu is active
    PIM_MENU_ACTIVE = (By.XPATH, "//a[contains(@class,'active')]/span[text()='PIM']")
    def is_pim_menu_opened(self) -> bool:
        """
        Returns True if the PIM menu is active/visible, else False
        """
        try:
            self.timeout = 30  # longer wait
            self.find_element(self.PIM_MENU_ACTIVE)
            return True
        except TimeoutException:
            return False