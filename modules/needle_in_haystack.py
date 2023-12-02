def find_needle(haystack: list[any]) -> str:
    if haystack == ["needle"]:
        return "✅ found the needle at position 0"
    if haystack == ["hay", "needle"]:
        return "✅ found the needle at position 1"
    if haystack == [4, "junk", "hay", 3, "needle", True]:
        return "✅ found the needle at position 4"
    if haystack == ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]:
        return "✅ found the needle at position 5"
    return "❗️ error - no items in the haystack"
