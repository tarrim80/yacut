from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import URL, DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    """Главная форма приложения."""

    original_link = TextAreaField(
        "Длинная ссылка",
        validators=(DataRequired(message="Обязательное поле"), URL()),
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=(Length(1, 16), Optional()),
    )
    submit = SubmitField("Создать")
