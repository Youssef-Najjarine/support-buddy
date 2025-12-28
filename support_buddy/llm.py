import os
from typing import Optional

from openai import OpenAI
from openai import RateLimitError

class LLMError(Exception):
    pass


def generate_response(*, system_prompt: str, user_prompt: str, temperature: float = 0.7) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-5.2")

    if not api_key:
        raise LLMError("Missing OPENAI_API_KEY. Add it to your .env file (not .env.example).")

    client = OpenAI(api_key=api_key)

    try:
        resp = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
    except RateLimitError as e:
        raise LLMError(
            "OpenAI API quota/billing issue (429). "
            "Go to the OpenAI Platform billing page, add a payment method or credits, "
            "then try again."
        ) from e
    except Exception as e:
        raise LLMError(f"LLM request failed: {e}") from e


    content: Optional[str] = resp.choices[0].message.content
    return (content or "").strip()
