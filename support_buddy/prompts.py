def stub_friend_response(problem_type: str, user_text: str) -> str:
    return (
        f"That sounds really tough. I’m here with you.\n\n"
        f"Before we solve it, quick question: what part feels heaviest right now?\n\n"
        f"(tag: {problem_type})"
    )

def stub_coach_response(problem_type: str, user_text: str) -> str:
    return (
        f"Okay — let’s turn this into something manageable.\n\n"
        f"1) What’s the outcome you want?\n"
        f"2) What’s the main obstacle?\n"
        f"3) What’s one small step you can do today?\n\n"
        f"(tag: {problem_type})"
    )

def stub_balanced_response(problem_type: str, user_text: str) -> str:
    return (
        f"I get why this is weighing on you.\n\n"
        f"Let’s do this in two parts:\n"
        f"- **One small step today:** write the situation in 1 sentence.\n"
        f"- **One helpful next move:** pick the easiest action you can do in 10 minutes.\n\n"
        f"Quick question: what’s the most urgent thing you need—comfort, a plan, or a script?\n\n"
        f"(tag: {problem_type})"
    )
