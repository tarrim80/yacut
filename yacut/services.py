import random
import string

from yacut.models import URLMap


def get_unique_short_id():
    """Создание уникального короткого идентификатора."""
    short = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    if URLMap.query.filter_by(short=short).first():
        get_unique_short_id()
    return short
