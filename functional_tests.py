import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # I as an user must enter the home page
        self.browser.get("http://localhost:8000")

        # Find the title with a To-Do list
        self.assertIn("To-Do", self.browser.title)

        # and find the header with also to-do list.
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # I'm invited to type a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # which is "Greet the world into the textbox"
        inputbox.send_keys('Greet the world')

        # After hitting enter, the page must update, listing a new task
        # "1: Greet the world into the textbox"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Greet the world' for row in rows),
            "New to-do item did not appear in table"
        )

        # There's still a textbox present to add another item
        # enters "Test everything!"
        self.fail('Finish the test!')

        # The page updates again showing both items in the list