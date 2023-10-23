from http import HTTPStatus

from flask import abort, flash, redirect, render_template, url_for

from yacut import app, db
from yacut.constants import EMPTY_INPUT, HTTPMethod, MessageInfo
from yacut.forms import URLMapForm
from yacut.models import URLMap
from yacut.services import get_unique_short_id
from yacut.validators import custom_id_validator


@app.route("/", methods=(HTTPMethod.GET, HTTPMethod.POST))
def index_view():
    """Главная страница приложения."""
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template("index.html", form=form)
    short = form.custom_id.data
    if URLMap.query.filter_by(short=short).first():
        flash(MessageInfo.SHORT_ALREADY_EXIST)
        return render_template("index.html", form=form)
    if not custom_id_validator(short):
        flash(MessageInfo.SHORT_INVALID)
        return render_template("index.html", form=form)
    original = form.original_link.data
    url = URLMap.query.filter_by(original=original).first()
    if url:
        link = url_for("redirect_view", short=url.short, _external=True)
        flash(
            f'{MessageInfo.ORIGINAL_ALREADY_EXIST}\n<a href="{link}">{link}</a>'
        )
        return render_template("index.html", form=form)
    if short in EMPTY_INPUT:
        short = get_unique_short_id()
    url = URLMap(original=form.original_link.data, short=short)
    db.session.add(url)
    db.session.commit()
    new_link = url_for("redirect_view", short=short, _external=True)
    flash(f'{MessageInfo.SHORT_DONE}\n<a href="{new_link}">{new_link}</a>')
    return render_template("index.html", form=form)


@app.route("/<short>")
def redirect_view(short):
    """Перенаправление по ссылке."""
    url = URLMap.query.filter_by(short=short).first()
    return redirect(url.original) if url else abort(HTTPStatus.NOT_FOUND)
