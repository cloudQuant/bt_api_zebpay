from __future__ import annotations

from typing import Any

from bt_api_base.error import ErrorCategory, ErrorTranslator, UnifiedError, UnifiedErrorCode


class ZebpayErrorTranslator(ErrorTranslator):
    @classmethod
    def translate(cls, raw_error: dict[str, Any], venue: str) -> UnifiedError | None:
        code_value = raw_error.get("code", 0)
        msg = str(raw_error.get("message", raw_error.get("error", "")))
        lower = msg.lower()
        if code_value == 401 or "auth" in lower:
            code = UnifiedErrorCode.INVALID_API_KEY
            category = ErrorCategory.AUTH
        elif code_value == 403 or "signature" in lower:
            code = UnifiedErrorCode.INVALID_SIGNATURE
            category = ErrorCategory.AUTH
        elif "balance" in lower or "insufficient" in lower:
            code = UnifiedErrorCode.INSUFFICIENT_BALANCE
            category = ErrorCategory.BUSINESS
        elif "rate" in lower or "limit" in lower:
            code = UnifiedErrorCode.RATE_LIMIT_EXCEEDED
            category = ErrorCategory.RATE_LIMIT
        else:
            code = UnifiedErrorCode.INTERNAL_ERROR
            category = ErrorCategory.SYSTEM
        return UnifiedError(
            code=code,
            category=category,
            venue=venue,
            message=msg or "Unknown error",
            original_error=str(raw_error),
            context={"raw_response": raw_error},
        )
