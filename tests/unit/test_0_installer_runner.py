import os

from modules import needle_in_haystack


def describe_needle_in_haystack():
    def should_error_when_input_is_empty_array(capsys):
        """🧪 should give the error no items in the haystack when the haystack is []"""
        assert needle_in_haystack.find_needle([]) == "❗️ error - no items in the haystack"
