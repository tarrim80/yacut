BASE_SHORT_URL = "http://localhost/"
PATTERN = r"^[a-zA-Z0-9]{1,16}$"
EMPTY_INPUT = ("", None)


class MessageInfo:
    NO_BODY_REQUEST = "Отсутствует тело запроса"

    ORIGINAL_ALREADY_EXIST = "Эта длинная ссылка уже была укорочена:"
    ORIGINAL_MISSING = '"url" является обязательным полем!'

    SHORT_ALREADY_EXIST = (
        "Предложенный вариант короткой ссылки уже существует."
    )
    SHORT_DONE = "Ваша новая ссылка готова:"
    SHORT_INVALID = "Указано недопустимое имя для короткой ссылки"
    SHORT_NOT_FOUND = "Указанный id не найден"
