from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('to-do', self.browser.title.lower())
        self.fail('Finish the test!')

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')  # user hears of new website and tries it out

if __name__ == '__main__':
    unittest.main()

# user is immediately prompted to enter a to-do item straight away

# user types in an item into a a text box

# when the user hits enter, the page updates and now the page lists the expected text from the previous box

# there is still an available text box, user adds another item

# the page updates and shows both items

# user checks that there is a unique URL to indicate that their to-do list will be saved

# user visits that URL, to-do list is still there
