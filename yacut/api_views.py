from http import HTTPStatus

from flask import jsonify, request

from yacut import app, db
from yacut.constants import EMPTY_INPUT, HTTPMethod, MessageInfo
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.services import get_unique_short_id
from yacut.validators import custom_id_validator


@app.route("/api/id/<short_id>/", methods=(HTTPMethod.GET,))
def get_original_url(short_id):
    """Получение оригинальной ссылки по короткому идентификатору."""
    url = URLMap().query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage(
            MessageInfo.SHORT_NOT_FOUND, HTTPStatus.NOT_FOUND
        )
    return jsonify({"url": url.to_dict()["url"]}), HTTPStatus.OK


@app.route("/api/id/", methods=(HTTPMethod.POST,))
def create_short_link():
    """Создание короткой ссылки."""
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage(MessageInfo.NO_BODY_REQUEST)
    if "url" not in data:
        raise InvalidAPIUsage(MessageInfo.ORIGINAL_MISSING)
    if "custom_id" not in data or data["custom_id"] in EMPTY_INPUT:
        data["custom_id"] = get_unique_short_id()
    if not custom_id_validator(data["custom_id"]):
        raise InvalidAPIUsage(MessageInfo.SHORT_INVALID)
    if URLMap.query.filter_by(short=data["custom_id"]).first() is not None:
        raise InvalidAPIUsage(MessageInfo.SHORT_ALREADY_EXIST)
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
