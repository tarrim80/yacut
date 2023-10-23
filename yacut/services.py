import random

from yacut.constants import LETTERS_AND_DIGITS_SET
from yacut.models import URLMap


def get_unique_short_id():
    """Создание уникального короткого идентификатора."""
    short = "".join(random.choices(LETTERS_AND_DIGITS_SET, k=6))
    if URLMap.query.filter_by(short=short).first():
        get_unique_short_id()
    return short
