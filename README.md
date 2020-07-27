# Турнир, 1 этап

Первый этап турнира по Python, вам предстоит долгий и тернистый путь, но я верю - вы справитесь.
На данном этапе вам предстоит выполнить 3+1 задание, каждое оценивается в 25 баллов.

## **25 баллов**

### Сортировка

#### Описание

На endpoint `/sort` отправляется POST запрос с json телом, в этом теле есть массив, который нужно отсортировать и тип сортировки - восходящая или снисходящая сортировка

###### Example

```sh

========REQUEST

POST /sort
Content-Type: application/json
{
    asc: true,
    array: [{"_id": "80808080", "name": "Gosha"}, {"_id": "90909090", "name": "Anton"}]
}

========RESPONSE

{
    success: true,
    data: [{"_id": "80808080", "name": "Anton"}, {"_id": "90909090", "name": "Gosha"}]
}
```

### Поиск + Поиск без регистра

#### Описание

На endpoint `/search` отправлявется POST запрос с json телом, в этом теле есть аттрибуты: string, search, match, где
string - это строка, по которой будет вестись поиск;
search - это строка, с помощью которой будет вестить поиск;
match - тип поиска, значения которой должны быть `"any"` или `"exact"`
ignorecase - будет-ли поиск вестись с учётом регистра или нет. Принимаемые значения `true` или `false`
Параметры ignorecase или match, если не будут указаны в теле запроса, то принимаются стандартные значения для match - это `"any"`, а для ignorecase - `true`

Ответом должен служить массив найденных индексов откуда начинается найденное слово или слова в строке.

###### Example

```sh
========REQUEST
POST /search
Content-Type: application/json
{
    string: "texttext"
    search: "text"
    match: "any"
}

========RESPONSE

{
    success: true,
    data: [0, 4]
}
```

```sh
========REQUEST
POST /search
Content-Type: application/json
{
    string: "sampletext"
    search: "text"
    match: "exact"
}

========RESPONSE

{
    success: true,
    data: []
}
```

```sh
========REQUEST
POST /search
Content-Type: application/json
{
    "string": "sampletext"
    "search": "TEXT"
    "match": "exact",
    "ignorecase": false
}

========RESPONSE

{
    success: true,
    data: []
}

```

### Парсинг сайта


#### Описание


На endpoint `/parse` требуется найти всё по заданному параметру search, на сайте [pep8](https://www.python.org/dev/peps/pep-0008/), если параметри search не будет указан, то необходимо вернуть информационную таблицу на сайте [pep8](https://www.python.org/dev/peps/pep-0008/)

##### Информационная таблица - Пример

```text
PEP: 8
Title: Style Guide for Python Code
Author: Guido van Rossum <guido at python.org>, Barry Warsaw <barry at python.org>, Nick Coghlan <ncoghlan at gmail.com>
Status: Active
Type: Process
Created: 05-Jul-2001
Post-History: 05-Jul-2001
```

###### Example

```sh

========REQUEST

GET /parse

========RESPONSE
{
    success: true,
    data: "PEP: 8
    Title: Style Guide for Python Code
    Author: Guido van Rossum <guido at python.org>, Barry Warsaw <barry at python.org>, Nick Coghlan <ncoghlan at gmail.com>
    Status: Active
    Type: Process
    Created: 05-Jul-2001
    Post-History: 05-Jul-2001"
}


========REQUEST

GET /parse?search=import

========RESPONSE
{
    success: true,
    data: [
        {
            "p": ["A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important."]
        },
        {
            "a": ["Imports"]
        },
        {
            "pre": ["# Correct: import os import sys", "# Wrong: import sys, os"]
        },
        ...
    ]
}

```

## Бонус

Бонус засчитывается при условии, что выполнены основные задания.

### Парсинг сайта + скачивание (25 баллов)

Сайт python, скачиваем конкретную версию.

```sh

========REQUEST

GET /download?python=3.8

========RESPONSE
{
    success: true,
    data: {
        "url": "http://127.0.0.1/download/{hash}"
    }
}
```

Скачивается на АПИ питон последней версии. Генерирует динамическую URL для скачивания и передаёт в ответе ссылку на этот файл

## Как отправить задание на проверку

Нажмите на кнопку Fork в правом, верхнем углу.
![Click to fork](https://i.imgur.com/oXsDTRI.png)
Склонируйте **только что полученный репозиторий** к себе
После чего запушьте изменения на свой репозиторий. Как только вы будете готовы отправить финальное решение для турнира, то создайте новый Pull Request для этого репозитория для ветки master.

![pull requests](https://i.imgur.com/xPYvnj1.png)
