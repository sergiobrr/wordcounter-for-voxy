"""
Simple BeeWare App to count words
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import re


def count_words(sentence: str) -> int:
    if not isinstance(sentence, str):
        raise TypeError("expected string")

    return len(re.findall(r'\w+', sentence))


class WordCounter(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return WordCounter()
