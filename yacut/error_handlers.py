from http import HTTPStatus
from typing import Optional

from flask import jsonify, render_template
from werkzeug import Response

from yacut import app, db


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(
        self, message: str, status_code: Optional[HTTPStatus] = None
    ) -> None:
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self) -> dict[str, str]:
        return dict(message=self.message)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error: InvalidAPIUsage) -> tuple[Response, HTTPStatus]:
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error: InvalidAPIUsage) -> tuple[str, HTTPStatus]:
    return render_template("404.html"), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error: InvalidAPIUsage) -> tuple[str, HTTPStatus]:
    db.session.rollback()  # type: ignore
    return render_template("500.html"), HTTPStatus.INTERNAL_SERVER_ERROR
