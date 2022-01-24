from app import *
import pytest


def test_hello():
    got = hello("Dominik")
    want = "Hello Dominik"

    assert got == want


testdata = ["I think today will be a great day",
            "I do not think this will turn out well"]


@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0


testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
]


@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):
    assert text_contain_word(word, sample) == expected_output


testdata = [([4, 4, 2, 1, 0], [0, 1, 2, 4, 4]),
            ([1, 3, 3, 4, 3, 3], [1, 3, 3, 3, 3, 4]
             ), ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])]


@ pytest.mark.parametrize('input, expected_output', testdata)
def test_bubble_sort_logic(input, expected_output):
    assert bubble_sort(input) == expected_output


def test_bubble_sort_type_of_input_data():
    assert bubble_sort("input") == None


@ pytest.mark.parametrize('input, expected_output', testdata)
def test_bubble_sort_type_of_output_data(input, expected_output):
    assert type(bubble_sort(input)) == list