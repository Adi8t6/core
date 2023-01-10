"""Constants for Google Assistant SDK integration."""
from typing import Final

DOMAIN: Final = "google_assistant_sdk"

DEFAULT_NAME: Final = "Google Assistant SDK"

CONF_LANGUAGE_CODE: Final = "language_code"

# https://developers.google.com/assistant/sdk/reference/rpc/languages
SUPPORTED_LANGUAGE_CODES: Final = [
    "de-DE",
    "en-AU",
    "en-CA",
    "en-GB",
    "en-IN",
    "en-US",
    "es-ES",
    "es-MX",
    "fr-CA",
    "fr-FR",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "pt-BR",
]

CONF_ENABLE_CONVERSATION_AGENT: Final = "enable_conversation_agent"
