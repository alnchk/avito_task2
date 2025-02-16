### Шаблон багрепорта

__id:__

__Приоритет:__

__Название:__

__Предусловия:__

__Тестовые данные:__

__Шаги:__

__Ожидаемый результат:__

__Фактический результат:__

__Комментарий:__

-----

# Баги


__id:__ BR1

__Приоритет:__ high

__Название:__
Неверное поле name у новых созданных объявлений

__Предусловия:__
Создать объявление (тест-кейс QAI1) и сохранить идентификатор объявления и параметры запроса.

Запрос Postman: Body -> Raw -> JSON:

```json
{
  "sellerID": 252677,
  "name": "Приблуда",
  "price": 255,
  "statistics":{
    "contacts":3,
    "likes":123,
    "viewCount":12
  }
}
```

Headers:
Content-Type: application/json,
Accept: application/json


__Шаги:__
Отправить GET запрос https://qa-internship.avito.com/api/1/item/:id где :id это идентификатор объявления, полученный в предусловии


__Ожидаемый результат:__

поле name у полученного объявления будет "Приблуда"

__Фактический результат:__

respons body:

```json
[
    {
        "createdAt": "2025-02-16 23:34:17.017088 +0300 +0300",
        "id": "a3daede9-85d2-419a-a92c-05a541144c6b",
        "name": "dsdsd",
        "price": 255,
        "sellerId": 252677,
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12
        }
    }
]
```
поле name = "dsdsd"

__Комментарий:__

-----

__id:__ BR2

__Приоритет:__ high

__Название:__ В объявлениях по идентификатору продавца перепутаны id и name

__Предусловия:__
Создать объявление (тест-кейс QAI1) и сохранить идентификатор объявления и параметры запроса.
Повторить создание объявления с теми же параметрами, сохранить id второго объявления.

Запрос Postman: Body -> Raw -> JSON:

```json
{
  "sellerID": 252677,
  "name": "Приблуда",
  "price": 255,
  "statistics":{
    "contacts":3,
    "likes":123,
    "viewCount":12
  }
}
```


Headers:
Content-Type: application/json,
Accept: application/json


__Тестовые данные:__

__Шаги:__

Отправить GET запрос https://qa-internship.avito.com/api/1/:sellerID/item где :sellerID из объявления из предусловия

__Ожидаемый результат:__
Сервер пришлет ответ с:

HTTP Status: 200 OK

и телом в формате JSON вида:

```json
[
    {
        "createdAt": "2025-02-16 23:34:17.017088 +0300 +0300",
        "id": "uuid1",
        "name": "Приблуда",
        "price": 255,
        "sellerId": 252677,
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12
        }
    },
    {
        "createdAt": "2025-02-16 23:34:17.017088 +0300 +0300",
        "id": "uuid2",
        "name": "Приблуда",
        "price": 255,
        "sellerId": 252677,
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12
        }
    },
]
__Фактический результат:__
приходит ответ вида:

```json
[
    {
        "createdAt": "2025-02-16 13:41:46.859778 +0300 +0300",
        "id": "dsdsd",
        "name": "7127a522-0209-4963-bd9d-3d0b2700198f",
        "price": 1,
        "sellerId": 252677,
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12
        }
    },
    {
        "createdAt": "2025-02-16 13:44:12.774149 +0300 +0300",
        "id": "dsdsd",
        "name": "bd72ae37-c947-4265-b581-de6acff7cdd4",
        "price": 1000,
        "sellerId": 252677,
        "statistics": {
            "contacts": 0,
            "likes": 0,
            "viewCount": 0
        }
    },
```
В поле name объявления стоит id и наоборот в поле id стоит name.

__Комментарий:__

-----


__id:__ BR3

__Приоритет:__ high

__Название:__ Возвращается неверная статистика по ручке "Получить статистику по айтем id"

__Предусловия:__

Создать объявление (тест-кейс QAI1) и сохранить идентификатор объявления и параметры запроса.

Запрос Postman: Body -> Raw -> JSON:

```json
{
  "sellerID": 252677,
  "name": "Приблуда",
  "price": 255,
  "statistics":{
    "contacts":3,
    "likes":123,
    "viewCount":12
  }
}
```

Headers:
Content-Type: application/json,
Accept: application/json


__Тестовые данные:__

__Шаги:__
Отправить GET запрос https://qa-internship.avito.com/api/1/statistic/:id


__Ожидаемый результат:__
Сервер пришлет ответ с:

HTTP Status: 200 OK

и телом в формате JSON:
```json
[
  {
    "contacts":3,
    "likes":123,
    "viewCount":12
  }
]
```
__Фактический результат:__
response body:

```json
[
    {
        "contacts": 3,
        "likes": 246,
        "viewCount": 258
    }
]
```
не совпадает likes и viewCount

__Комментарий:__

-----


__id:__ BR4

__Приоритет:__ high

__Название:__ Возможно создание объявления без поля name

__Предусловия:__
Headers:
Content-Type: application/json,
Accept: application/json

__Тестовые данные:__
Запрос Postman: Body -> Raw -> JSON:

```json
{
  "sellerID": 252677,
  "price": 255,
  "statistics":{
    "contacts":3,
    "likes":123,
    "viewCount":12
  }
}
```

__Шаги:__
Отправить POST запрос https://qa-internship.avito.com/api/1/item


__Ожидаемый результат:__

Пришел ответ, в котором:

HTTP Status: 400 Bad Request

тело ответа в формате JSON и имеет вид:

{
  "result": {
    "messages": {

    },
    "message": "<string>"
  },
  "status": "<string>"
}
__Фактический результат:__

Объявление создаётся, статус ответа 200


__Комментарий:__

-----


__id:__ BR5

__Приоритет:__ high

__Название:__ Возможно создание объявления без поля price

__Предусловия:__
Headers:
Content-Type: application/json,
Accept: application/json

__Тестовые данные:__
Запрос Postman: Body -> Raw -> JSON:

```json
{
  "sellerID": 252677,
  "name": "Приблуда",
  "statistics":{
    "contacts":3,
    "likes":123,
    "viewCount":12
  }
}
```

__Шаги:__
Отправить POST запрос https://qa-internship.avito.com/api/1/item


__Ожидаемый результат:__

Пришел ответ, в котором:

HTTP Status: 400 Bad Request

тело ответа в формате JSON и имеет вид:

{
  "result": {
    "messages": {

    },
    "message": "<string>"
  },
  "status": "<string>"
}
__Фактический результат:__

Объявление создаётся, статус ответа 200
если найти его по ид, то price будет 0


__Комментарий:__

-----

__id:__ BR6

__Приоритет:__ high

__Название:__ Возможно создание объявления без поля sellerID

__Предусловия:__
Headers:
Content-Type: application/json,
Accept: application/json

__Тестовые данные:__
Запрос Postman: Body -> Raw -> JSON:

```json
{
  "name": "Приблуда",
  "price": 255,
  "statistics":{
    "contacts":3,
    "likes":123,
    "viewCount":12
  }
}
```

__Шаги:__
Отправить POST запрос https://qa-internship.avito.com/api/1/item


__Ожидаемый результат:__

Пришел ответ, в котором:

HTTP Status: 400 Bad Request

тело ответа в формате JSON и имеет вид:

{
  "result": {
    "messages": {

    },
    "message": "<string>"
  },
  "status": "<string>"
}
__Фактический результат:__

Объявление создаётся, статус ответа 200
если найти его по ид, то sellerId будет 0

__Комментарий:__

-----
