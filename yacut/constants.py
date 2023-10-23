import string

BASE_SHORT_URL = "http://localhost/"
EMPTY_INPUT = ("", None)
MIN_SHORT_LENGHT = 1
MAX_SHORT_LENGHT = 16
SHORT_VALIDATION_PATTERN = rf"^[a-zA-Z0-9]{{{MIN_SHORT_LENGHT},{MAX_SHORT_LENGHT}}}$"  # Паттерн проверки короткой ссылки на соответствие заданию
LETTERS_AND_DIGITS_SET = string.ascii_letters + string.digits


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


class HTTPMethod:
    GET = "GET"
    POST = "POST"
