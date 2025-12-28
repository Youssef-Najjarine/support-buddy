from support_buddy.llm import generate_response
from support_buddy.prompts import build_prompts
from support_buddy.safety import is_crisis
from support_buddy.memory import MemoryStore


def classify_problem(user_text: str) -> str:
    t = user_text.lower()

    if any(w in t for w in ["anxious", "anxiety", "panic", "stressed", "stress", "overwhelmed"]):
        return "stress"
    if any(w in t for w in ["girlfriend", "boyfriend", "wife", "husband", "partner", "relationship", "fight", "argument"]):
        return "relationship"
    if any(w in t for w in ["interview", "job", "resume", "boss", "coworker", "work"]):
        return "career"
    if any(w in t for w in ["focus", "procrastinate", "productivity", "motivation"]):
        return "productivity"
    return "general"


def route_message(user_text: str, style: str, memory: MemoryStore) -> str:
    if is_crisis(user_text):
        return (
            "I’m really sorry you’re feeling this way. You don’t have to handle this alone.\n\n"
            "If you’re in immediate danger or might hurt yourself, call your local emergency number right now.\n"
            "If you’re in the U.S. or Canada, you can call or text 988.\n\n"
            "If you want, tell me where you are (country/state) and whether you’re safe right now."
        )

    problem_type = classify_problem(user_text)

    system_prompt, user_prompt = build_prompts(
        style=style,
        problem_type=problem_type,
        user_text=user_text,
    )

    return generate_response(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0.7)
