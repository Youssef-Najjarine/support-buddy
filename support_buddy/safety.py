def is_crisis(text: str) -> bool:
    t = text.lower()
    crisis_phrases = [
        "kill myself", "end my life", "suicide", "want to die",
        "hurt myself", "self harm", "self-harm",
    ]
    return any(p in t for p in crisis_phrases)
