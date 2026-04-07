from __future__ import annotations

import asyncio
import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


@dataclass(slots=True)
class RuntimeSettings:
    rate_limit_per_minute: int = 60
    poll_interval_seconds: int = 3
    poll_timeout_seconds: int = 120


class CredentialManager:
    def __init__(self) -> None:
        self._lock = asyncio.Lock()
        self._api_key: Optional[str] = None
        self._env_key: Optional[str] = os.getenv("IXSPY_API_KEY")

    async def get_api_key(self) -> Optional[str]:
        async with self._lock:
            return self._api_key or self._env_key

    async def set_api_key(self, value: str | None) -> None:
        async with self._lock:
            self._api_key = value or None

    def masked_suffix(self) -> Optional[str]:
        value = self._api_key or self._env_key
        if not value:
            return None
        return f"...{value[-4:]}"
