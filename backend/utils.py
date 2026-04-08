"""Shared utility helpers for backend services."""

import tiktoken


def estimate_token_count(text: str, model: str = "gpt-4") -> int:
    """Estimate token count for markdown content using tiktoken."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))
