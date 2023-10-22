from http import HTTPStatus

from flask import jsonify, request

from yacut import app, db
from yacut.constants import EMPTY_INPUT
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.services import get_unique_short_id
from yacut.validators import custom_id_validator


@app.route("/api/id/<short_id>/", methods=("GET",))
def get_short_link(short_id):
    url = URLMap().query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage("Указанный id не найден", HTTPStatus.NOT_FOUND)
    return jsonify({"url": url.to_dict()["url"]}), HTTPStatus.OK


@app.route("/api/id/", methods=("POST",))
def create_id():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage("Отсутствует тело запроса")
    if "url" not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if "custom_id" not in data or data["custom_id"] in EMPTY_INPUT:
        data["custom_id"] = get_unique_short_id()
    if not custom_id_validator(data["custom_id"]):
        raise InvalidAPIUsage("Указано недопустимое имя для короткой ссылки")
    if URLMap.query.filter_by(short=data["custom_id"]).first() is not None:
        raise InvalidAPIUsage(
            "Предложенный вариант короткой ссылки уже существует."
        )
    url = URLMap.query.filter_by(original=data["url"]).first()
    if url is not None:
        return jsonify(url.to_dict()), HTTPStatus.OK
    new_data = {
        "original": data.get("url", ""),
        "short": data.get("custom_id", ""),
    }
    url = URLMap()
    url.from_dict(data=new_data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED
