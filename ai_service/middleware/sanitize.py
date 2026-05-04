def sanitize_input(text):
    if not text or text.strip() == "":
        return None

    blocked_patterns = [
        "<script>",
        "</script>",
        "ignore previous instructions",
        "forget previous instructions",
        "<",
        ">"
    ]

    lower_text = text.lower()

    for pattern in blocked_patterns:
        if pattern in lower_text:
            return None

    return text.strip()