from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class MemoryStore:
    max_turns: int = 8
    turns: List[Tuple[str, str]] = field(default_factory=list)

    def add_turn(self, user: str, buddy: str) -> None:
        self.turns.append((user, buddy))
        if len(self.turns) > self.max_turns:
            self.turns = self.turns[-self.max_turns:]

    def last_user_messages(self, n: int = 3) -> List[str]:
        users = [u for (u, _) in self.turns]
        return users[-n:]
