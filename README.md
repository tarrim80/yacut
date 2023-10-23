<h1>Финальный проект спринта: сервис YaCut</h1>

<h2>Проект YaCut</h2>
<div class="paragraph">На большинстве сайтов адреса страниц довольно длинные, например, как у той страницы, на которой вы сейчас находитесь. Делиться такими длинными ссылками не всегда удобно, а иногда и вовсе невозможно. 
</div>
<div class="paragraph">Удобнее использовать короткие ссылки. Например, ссылки 
<a href="http://yacut.ru/lesson" target="_blank">http://yacut.ru/lesson</a> и <a href="http://yacut.ru/12e07d">http://yacut.ru/12e07d</a> воспринимаются лучше, чем <a href="https://practicum.yandex.ru/trainer/backend-developer/lesson/12e07d96-31f3-449f-abcf-e468b6a39061/" target="_blank">https://practicum.yandex.ru/trainer/backend-developer/lesson/12e07d96-31f3-449f-abcf-e468b6a39061/</a>. 
</div>
<div class="paragraph">Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.
</div>
<h2>Задание</h2>
<div class="paragraph">Ваша задача — написать сервис укорачивания ссылок и API к нему. </div>
<div class="paragraph">Ключевые возможности сервиса:</div>
<ul>
<li>генерация коротких ссылок и связь их с исходными длинными ссылками,</li>
<li>переадресация на исходный адрес при обращении к коротким ссылкам.</li>
</ul>
<div class="paragraph">Пользовательский интерфейс сервиса — одна страница с формой. Эта форма должна состоять из двух полей:</div>
<ul>
<li>обязательного для длинной исходной ссылки;</li>
<li>необязательного для пользовательского варианта короткой ссылки.</li>
</ul>
<div class="paragraph">Пользовательский вариант короткой ссылки не должен превышать 16 символов.</div>

<div class="paragraph">Если пользователь предложит вариант короткой ссылки, который уже занят, то нужно сообщить пользователю об этом через уведомление: <code class="code-inline code-inline_theme_light">Предложенный вариант короткой ссылки уже существует.</code>. Существующая в базе данных ссылка должна остаться неизменной.</div>
<div class="paragraph">Если пользователь не заполнит поле со своим вариантом короткой ссылки, то сервис должен сгенерировать её автоматически. Формат для ссылки по умолчанию — шесть случайных символов, в качестве которых можно использовать:</div>
<ul>
<li>большие латинские буквы,</li>
<li>маленькие латинские буквы,</li>
<li>цифры в диапазоне от 0 до 9.</li>
</ul>
<div class="paragraph">Автоматически сгенерированная короткая ссылка должна добавляться в базу данных, но только если в ней ещё нет такого же идентификатора. В противном случае нужно генерировать идентификатор заново.</div>
<h3>API для проекта</h3>
<div class="paragraph">API проекта должен быть доступен всем желающим. Сервис должен обслуживать только два эндпоинта:</div>
<ul>
<li>/api/id/ — POST-запрос на создание новой короткой ссылки;</li>
<li>/api/id/&lt;short_id&gt;/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.</li>
</ul>
<div class="paragraph">Примеры запросов к API, варианты ответов и ошибок приведены в спецификации openapi.yml; спецификация есть в репозитории <code class="code-inline code-inline_theme_light">yacut</code>. </div>
<div class="paragraph">Для удобной работы с документом воспользуйтесь 
<a href="https://editor.swagger.io/" target="blank">онлайн-редактором Swagger Editor</a>, в котором можно визуализировать спецификацию.</div>
<h3>Коллекция запросов для Postman</h3>
<div class="paragraph">В директории <em>postman_collection</em> сохранена коллекция запросов для отладки и проверки работы текущей версии проекта YaCut.</div>
<div class="paragraph">Когда проект будет готов обрабатывать запросы к API — импортируйте коллекцию в Postman и выполняйте запросы.</div>
<h2>План работы</h2>
<ol start="1">
<li>Создайте новый Flask-проект и сразу опишите приложение в виде пакета.</li>
<li>Подключите к проекту ORM SQLAlchemy. На этапе разработки используйте базу данных SQLite.</li>
<li>Опишите модель <code class="code-inline code-inline_theme_light">URLMap</code>: в ней должны быть поля 
<ul>
<li><code class="code-inline code-inline_theme_light">id</code> — поле для ID,</li>
<li><code class="code-inline code-inline_theme_light">original</code> — поле для оригинальной длинной ссылки,</li>
<li><code class="code-inline code-inline_theme_light">short</code> — поле для короткого идентификатора,</li>
<li><code class="code-inline code-inline_theme_light">timestamp</code> — поле для временной метки.</li>
</ul>
</li>
<li>Опишите форму и валидаторы полей форм. Форма должна содержать поля:
<ul>
<li><code class="code-inline code-inline_theme_light">original_link</code> — поле для оригинальной длинной ссылки,</li>
<li><code class="code-inline code-inline_theme_light">custom_id</code> — поле для пользовательского варианта короткого идентификатора.</li>
</ul>
</li>
<li>Придумайте и реализуйте в функции <code class="code-inline code-inline_theme_light">get_unique_short_id()</code> алгоритм формирования коротких идентификаторов переменной длины. Логику формирования идентификатора выбирайте на своё усмотрение, мы предлагаем использовать функцию <code class="code-inline code-inline_theme_light">random()</code>.</li>
<li>Опишите view-функцию для главной страницы и view-функцию, которая будет отвечать за переадресацию.</li>
<li>Подключите и настройте статику проекта.</li>
<li>Из заготовки шаблона создайте базовый и подключаемые шаблоны, шаблон главной страницы и шаблон страниц ошибок</li>
<li>Напишите API для работы с сервисом. API-функции должны быть описаны в отдельном файле пакета приложения api_views.py.</li>
<li>Опишите собственные обработчики ошибок для пользовательского интерфейса и для API.</li>
</ol>


<h2  align="center"> Локальный запуск проекта </h2>

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:tarrim80/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Запустить приложение на локальном сервере:

```
flask run
```

<div align="center">

### Используемые технологии:

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python&logoColor=FFFFFF)](https://www.python.org/)&nbsp;&nbsp;![github](https://img.shields.io/badge/github-464646?style=flat-square&logo=github&logoColor=FFFFFF)&nbsp;&nbsp;![Flask](https://img.shields.io/badge/-Flask-464646?style=flat&logo=Flask&logoColor=white&link=https%3A%2F%2Fflask.palletsprojects.com%2Fen%2F3.0.x%2F)&nbsp;&nbsp;![Jinja](https://img.shields.io/badge/-jinja-464646?style=flat&logo=jinja&logoColor=white&link=https%3A%2F%2Fjinja.palletsprojects.com%2Fen%2F3.1.x%2F)&nbsp;&nbsp;![HTML](https://img.shields.io/badge/-HTML-464646?style=flat&logo=HTML5&logoColor=white)&nbsp;&nbsp;![CSS](https://img.shields.io/badge/-CSS-464646?style=flat&logo=CSS3&logoColor=white)&nbsp;&nbsp;![Insomnia](https://img.shields.io/badge/-Insomnia-464646?style=flat&logo=Insomnia&logoColor=white&link=https%3A%2F%2Finsomnia.rest%2F)&nbsp;&nbsp;![Postman](https://img.shields.io/badge/-Postman-464646?style=flat&logo=Postman&logoColor=white)&nbsp;&nbsp;![Swagger](https://img.shields.io/badge/-Swagger-464646?style=flat&logo=Swagger&logoColor=white&link=https%3A%2F%2Fswagger.io%2F)
</div>
<div align="center">

### Выполнено в рамках прохождения курса "Python-разработчик плюс" на ["Яндекс&nbsp;Практикум"](https://practicum.yandex.ru/)
</div>
