from selenium import webdriver
from selenium.webdriver.common.by import By
from budget.models import Project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import os
import time
#os.environ["webdriver.chrome.driver"] = "/media/kamal/DATA/temp_installers/chrome-linux64/chrome"

class TestProjectListPage(StaticLiveServerTestCase):
   
    def setUp(self):
        #service = webdriver.ChromeService(executable_path = '/usr/bin/chromedriver')
        service = webdriver.ChromeService(executable_path = 'functional_tests/chromedriver')
        self.browser = webdriver.Chrome(service=service)
        #driver = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()


    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        #time.sleep(20)

        alert = self.browser.find_element(By.CLASS_NAME, "noproject-wrapper")
        #alert = self.browser.find_element_by_class_name('noproject-wrapper')
        self.assertEquals(
            alert.find_element(By.TAG_NAME,'h3').text,
            'Sorry, you don\'t haev any projects, yet.'
        )
    
    def test_user_clicks_button(self):

        self.browser.get(self.live_server_url)
        #time.sleep(20)

        self.browser.find_element(By.TAG_NAME, "a").click()

        add_url = self.live_server_url + reverse('add') 
        #add_url = self.live_server_url 

        self.assertEquals(
            self.browser.current_url,
            add_url
        )
       
    def test_user_sees_project_list(self):

        project1 = Project.objects.create(
            name = 'project1',
            budget = 10000
        )
        self.browser.get(self.live_server_url)
        #time.sleep(20)

        self.assertEquals(
            self.browser.find_element(By.TAG_NAME,'h5').text,
            'project1' 
        )

