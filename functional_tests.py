from re import S
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')  # note this is finding multiple elements in table
        self.assertIn(row_text, [row.text for row in rows])

    def enter_to_do_item(self, item_text):
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_placeholder = input_box.get_attribute('placeholder')
        self.assertEqual(input_placeholder, 'Enter a to-do item')

        input_box.send_keys(item_text)
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('To-Do', self.browser.title)
        
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text
        self.assertIn('To-Do', header_text)

        self.enter_to_do_item('Buy soup')
        self.enter_to_do_item('Cook soup')

        self.check_for_row_in_list_table('1: Buy soup')
        self.check_for_row_in_list_table('2: Cook soup')
        
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
