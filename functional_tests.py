import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # The user goes to check the homepage
        self.browser.get("http://localhost:8000")

        # The title and header must have to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail('Finish the test!')

