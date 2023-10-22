from datetime import datetime

from yacut import db
from yacut.constants import BASE_SHORT_URL


class URLMap(db.Model):
    """Главная модель приложения.

    Содержит длинную ссылку и соответствующий ей короткий вариант.
    """

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, unique=True, nullable=False)
    short = db.Column(db.String(16), nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            short_link=BASE_SHORT_URL + self.short,
            url=self.original,
        )

    def from_dict(self, data):
        for field in ("short", "original"):
            if field in data:
                setattr(self, field, data[field])
