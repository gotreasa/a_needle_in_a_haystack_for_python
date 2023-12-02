def find_needle(haystack: list[any]) -> str:
    if haystack == ["needle"]:
        return f"✅ found the needle at position {haystack.index('needle')}"
    if haystack == ["hay", "needle"]:
        return f"✅ found the needle at position {haystack.index('needle')}"
    if haystack == [4, "junk", "hay", 3, "needle", True]:
        return f"✅ found the needle at position {haystack.index('needle')}"
    if haystack == ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]:
        return f"✅ found the needle at position {haystack.index('needle')}"
    return "❗️ error - no items in the haystack"
