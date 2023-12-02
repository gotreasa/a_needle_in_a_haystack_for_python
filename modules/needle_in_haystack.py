def find_needle(haystack: list[any]) -> str:
    if haystack == []:
        return "❗️ error - no items in the haystack"
    if haystack.count("needle") > 1:
        return "❗️ error - there is more than one needle in the haystack"
    return f"✅ found the needle at position {haystack.index('needle')}"
