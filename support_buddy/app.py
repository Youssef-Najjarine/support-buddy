from support_buddy.router import route_message
from support_buddy.memory import MemoryStore
from dotenv import load_dotenv
load_dotenv()

def main() -> None:
    print("Support Buddy 🤝 (type 'exit' to quit)")
    memory = MemoryStore(max_turns=8)

    # Default style; user can change by typing: /style friend | /style coach | /style balanced
    style = "balanced"

    while True:
        user_text = input("\nYou: ").strip()
        if not user_text:
            continue
        if user_text.lower() in {"exit", "quit"}:
            print("Buddy: Talk soon. You’ve got this 🤝")
            break

        if user_text.startswith("/style"):
            parts = user_text.split(maxsplit=1)
            if len(parts) == 2 and parts[1].strip().lower() in {"friend", "coach", "balanced"}:
                style = parts[1].strip().lower()
                print(f"Buddy: Got it — style set to '{style}'.")
            else:
                print("Buddy: Usage: /style friend | /style coach | /style balanced")
            continue

        response = route_message(user_text=user_text, style=style, memory=memory)
        memory.add_turn(user_text, response)

        print(f"Buddy: {response}")

if __name__ == "__main__":
    main()
