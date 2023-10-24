from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from yacut import db
from yacut.constants import BASE_SHORT_URL, MAX_SHORT_LENGHT


class URLMap(db.Model):  # type: ignore
    """Главная модель приложения.

    Содержит длинную ссылку и соответствующий ей короткий вариант.
    """

    id = Column(Integer, primary_key=True)
    original = Column(Text, unique=True, nullable=False)
    short = Column(String(MAX_SHORT_LENGHT), nullable=True)
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)

    def to_dict(self) -> dict[str, str]:
        return dict(
            short_link=BASE_SHORT_URL + self.short,
            url=self.original,
        )

    def from_dict(self, data: dict[str, str]) -> None:
        for field in ("short", "original"):
            if field in data:
                setattr(self, field, data[field])
