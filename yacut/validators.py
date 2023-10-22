import re

from yacut.constants import PATTERN


def custom_id_validator(custom_id):
    """Валидатор предложенного короткого идентификатора."""
    if custom_id:
        return bool(re.match(PATTERN, custom_id))
    return True
