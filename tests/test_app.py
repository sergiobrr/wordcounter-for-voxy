import pytest
from wordcounter.app import count_words

sentence = """Lorem ipsum dolor sit amet.
Consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""


def test_count_words():
    assert count_words(sentence) == 19


def test_count_words_corner_cases():
    assert count_words("") == 0
    assert count_words(" ") == 0
    with pytest.raises(TypeError, match="expected string"):
        count_words({'a': 'b'})

    with pytest.raises(TypeError, match="expected string"):
        count_words(None)


def test_wrong_count_words():
    sentence = '123456abc   555%%%abc'

    with pytest.raises(TypeError):
        count_words(sentence)
