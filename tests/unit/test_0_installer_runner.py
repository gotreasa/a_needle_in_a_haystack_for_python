import os

from modules import needle_in_haystack


def describe_needle_in_haystack():
    def should_error_when_input_is_empty_array():
        """🧪 should give the error no items in the haystack when the haystack is []"""
        assert needle_in_haystack.find_needle([]) == "❗️ error - no items in the haystack"

    def should_find_needle_position_0():
        """🧪 should give the message found the needle at position 0 when the haystack is ["needle"]"""
        assert needle_in_haystack.find_needle(["needle"]) == "✅ found the needle at position 0"

    def should_find_need_at_position_1():
        """🧪 should give the message found the needle at position 1 when the haystack is ["hay", "needle"]"""
        assert needle_in_haystack.find_needle(["hay", "needle"]) == "✅ found the needle at position 1"
