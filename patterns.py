PATTERN_RULES = {
    "Sliding Window": {
        "keywords": ["subarray", "substring", "continuous"],
        "constraints": lambda n: n >= 10**4,
        "description": "Used when dealing with contiguous ranges and optimizing repeated calculations."
    },
    "Two Pointers": {
        "keywords": ["sorted", "pair", "palindrome"],
        "constraints": lambda n: True,
        "description": "Efficient traversal from both ends of a sequence."
    },
    "Hash Map": {
        "keywords": [
            "two sum",
            "pair",
            "target",
            "indices",
            "complement"
        ],
        "constraints": lambda n: n >= 2,
        "description": (
            "Hash maps allow constant-time lookups to check whether "
            "a complement value has already been seen, reducing "
            "time complexity from O(n²) to O(n)."
        )
    }
}  # 👈 THIS was missing

def detect_pattern(problem):
    title = problem["title"].lower()
    constraints = problem["constraints"]

    matches = []

    for pattern, rule in PATTERN_RULES.items():
        if (
            any(word in title for word in rule["keywords"])
            and rule["constraints"](constraints["n"])
        ):
            matches.append({
                "pattern": pattern,
                "description": rule["description"]
            })

    if not matches:
        return [{
            "pattern": "Unknown",
            "description": "Pattern not detected yet."
        }]

    return matches
