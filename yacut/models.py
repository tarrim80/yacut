from datetime import datetime

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, unique=True, nullable=False)
    short = db.Column(db.String(16), nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    # def to_dict(self):
    #     return dict(
    #         id=self.id,
    #         short=self.short,
    #         original=self.original,
    #         timestamp=self.timestamp,
    #     )

    # def from_dict(self, data):
    #     for field in ("short", "original"):
    #         if field in data:
    #             setattr(self, field, data[field])
