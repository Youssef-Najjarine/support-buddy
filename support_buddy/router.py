from support_buddy.safety import is_crisis
from support_buddy.prompts import stub_friend_response, stub_coach_response, stub_balanced_response
from support_buddy.memory import MemoryStore

def classify_problem(user_text: str) -> str:
    t = user_text.lower()

    if any(w in t for w in ["anxious", "anxiety", "panic", "stressed", "stress", "overwhelmed"]):
        return "stress"
    if any(w in t for w in ["girlfriend", "boyfriend", "wife", "husband", "partner", "relationship", "fight", "argument"]):
        return "relationship"
    if any(w in t for w in ["interview", "job", "resume", "boss", "coworker", "work"]):
        return "career"
    if any(w in t for w in ["focus", "procrastinate", "productivity", "motivation", "lazy"]):
        return "productivity"

    return "general"

def route_message(user_text: str, style: str, memory: MemoryStore) -> str:
    # 1) Safety gate
    if is_crisis(user_text):
        return (
            "I’m really sorry you’re feeling this way. You don’t have to handle this alone.\n\n"
            "If you’re in immediate danger or might hurt yourself, call your local emergency number right now.\n"
            "If you’re in the U.S. or Canada, you can call or text 988 (Suicide & Crisis Lifeline).\n\n"
            "If you want, tell me where you are (country/state) and whether you’re safe right now."
        )

    # 2) Classify
    problem_type = classify_problem(user_text)

    # 3) Respond by style (stub for now)
    if style == "friend":
        return stub_friend_response(problem_type, user_text)
    if style == "coach":
        return stub_coach_response(problem_type, user_text)

    return stub_balanced_response(problem_type, user_text)
