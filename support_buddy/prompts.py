def build_prompts(*, style: str, problem_type: str, user_text: str) -> tuple[str, str]:
    # System prompt controls personality + rules
    if style == "friend":
        system = (
            "You are Support Buddy, a warm best-friend style support chatbot. "
            "Be empathetic, non-judgmental, and encouraging. "
            "Do NOT claim to be a therapist or medical professional. "
            "Keep advice low-risk and practical."
        )
    elif style == "coach":
        system = (
            "You are Support Buddy, a direct but kind coach. "
            "Be concise, action-oriented, and structured. "
            "Do NOT claim to be a therapist or medical professional. "
            "Keep advice low-risk and practical."
        )
    else:
        system = (
            "You are Support Buddy, a supportive friend + practical coach. "
            "Be empathetic and also provide a clear plan. "
            "Do NOT claim to be a therapist or medical professional. "
            "Keep advice low-risk and practical."
        )

    # Format rules (deterministic “algorithm” you’re enforcing)
    format_rules = (
        "Reply in this exact structure:\n"
        "1) Validation: 1–2 sentences.\n"
        "2) Clarifying question: exactly 1 question.\n"
        "3) Action steps: 3 bullet points max.\n"
        "4) Optional: If it's a conversation problem, include a short 2–3 line script.\n"
        "Keep it under 160 words."
    )

    user = (
        f"Problem type: {problem_type}\n"
        f"User message: {user_text}\n\n"
        f"{format_rules}"
    )

    return system, user
