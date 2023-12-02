import os

from modules import needle_in_haystack


def describe_needle_in_haystack():
    def should_error_when_input_is_empty_array():
        """🧪 should give the error no items in the haystack when the haystack is []"""
        assert needle_in_haystack.find_needle([]) == "❗️ error - no items in the haystack"

    def should_find_needle_position_0():
        """🧪 should give the message found the needle at position 0 when the haystack is ["needle"]"""
        assert needle_in_haystack.find_needle(["needle"]) == "✅ found the needle at position 0"

    def should_find_needle_at_position_1():
        """🧪 should give the message found the needle at position 1 when the haystack is ["hay", "needle"]"""
        assert needle_in_haystack.find_needle(["hay", "needle"]) == "✅ found the needle at position 1"

    def should_find_needle_at_position_4_with_different_types():
        """🧪 should give the message found the needle at position 4 when the haystack is [4, "junk", "hay", 3, "needle", true]"""
        assert (
            needle_in_haystack.find_needle([4, "junk", "hay", 3, "needle", True]) == "✅ found the needle at position 4"
        )

    def should_find_needle_at_position_5_with_string_types():
        """🧪 should give the message found the needle at position 5 when the haystack is ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]"""
        assert (
            needle_in_haystack.find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"])
            == "✅ found the needle at position 5"
        )

    def should_error_when_there_is_more_than_one_needle():
        """🧪 should give the error there is more than one needle in the haystack when the haystack is ["needle", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]"""

        assert (
            needle_in_haystack.find_needle(["needle", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"])
            == "❗️ error - there is more than one needle in the haystack"
        )
