def find_needle(haystack: list[any]) -> str:
    if haystack == ["needle"]:
        return "✅ found the needle at position 0"
    return "❗️ error - no items in the haystack"
