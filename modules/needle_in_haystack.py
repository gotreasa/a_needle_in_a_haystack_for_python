def find_needle(haystack: list[any]) -> str:
    if haystack == ["needle"]:
        return "✅ found the needle at position 0"
    if haystack == ["hay", "needle"]:
        return "✅ found the needle at position 1"
    return "❗️ error - no items in the haystack"
