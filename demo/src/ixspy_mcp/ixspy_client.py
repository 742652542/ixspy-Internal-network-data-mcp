from __future__ import annotations

from ixspy_img_api import AIImageGenerator

from .config import CredentialManager, RuntimeSettings


class IxSpyClient:
    def __init__(self, credentials: CredentialManager, settings: RuntimeSettings | None = None) -> None:
        self._credentials = credentials
        self._settings = settings or RuntimeSettings()

    async def get_client(self) -> AIImageGenerator:
        api_key = await self._credentials.get_api_key()
        if not api_key:
            raise RuntimeError("API key not configured")
        return AIImageGenerator(api_key=api_key)
