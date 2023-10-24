import re
from typing import Optional

from yacut.constants import SHORT_VALIDATION_PATTERN


def custom_id_validator(custom_id: Optional[str]) -> bool:
    """Валидатор предложенного короткого идентификатора."""
    if custom_id:
        return bool(re.match(SHORT_VALIDATION_PATTERN, custom_id))
    return True
