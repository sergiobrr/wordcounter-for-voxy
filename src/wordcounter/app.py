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
        main_box = toga.Box(
            style=Pack(direction=COLUMN)
        )

        text_label = toga.Label(
            "Input sentence: ",
            style=Pack(padding=(10, 20))
        )
        self.phrase_input = toga.TextInput(
            style=Pack(flex=1)
        )

        phrase_box = toga.Box(
            style=Pack(direction=ROW, padding=(10, 20))
        )
        phrase_box.add(text_label)
        phrase_box.add(self.phrase_input)
        buttons_box = toga.Box(
            style=Pack(
                flex=1, direction=ROW, padding=(0, 10)
            )
        )
        button = toga.Button(
            "Count words!",
            on_press=self.count_words,
            style=Pack(flex=1, padding=10)
        )
        clear_button = toga.Button(
            "Clear",
            on_press=self.clear_phrase_input,
            style=Pack(flex=1, padding=10)
        )
        buttons_box.add(button)
        buttons_box.add(clear_button)

        self.result_label = toga.Label(
            "Result: ",
            style=Pack(padding=(10, 20))
        )

        result_box = toga.Box(
            style=Pack(direction=ROW, padding=(10, 20))
        )
        result_box.add(self.result_label)

        main_box.add(phrase_box)
        main_box.add(buttons_box)
        main_box.add(result_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def clear_phrase_input(self, widget):
        self.phrase_input.clear()

    def count_words(self, widget):
        try:
            self.result_label.text = f"Result: {count_words(self.phrase_input.value)}"
        except TypeError:
            self.main_window.info_dialog(
                "Error",
                "Input must be a string"
            )


def main():
    return WordCounter()
