from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import URL, DataRequired, Length, Optional

from yacut.constants import MAX_SHORT_LENGHT, MIN_SHORT_LENGHT


class URLMapForm(FlaskForm):
    """Главная форма приложения."""

    original_link = TextAreaField(
        "Длинная ссылка",
        validators=(DataRequired(message="Обязательное поле"), URL()),
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=(Length(MIN_SHORT_LENGHT, MAX_SHORT_LENGHT), Optional()),
    )
    submit = SubmitField("Создать")
