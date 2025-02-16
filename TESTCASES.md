# Тесткейсы


### Шаблон тескейса

__id:__

__Приоритет:__

__Название:__

__Предусловия:__

__Тестовые данные:__

__Шаги:__

__Ожидаемый результат:__

__Статус прохождения:__

__Bug report:__

__Комментарий:__

-----



__id:__ QAI1

__Приоритет:__ high

__Название:__ Создание нового объявления c корректными данными

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

Запрос успешно отправлен на сервер.

Пришел ответ, в котором:

HTTP Status: 200 OK

тело ответа в формате JSON и имеет вид:

{

  "status": "<string>"

}

где <string> вида: "Сохранили объявление - {id нового объявления}"



__Статус прохождения:__ PASSED

__Bug report:__

__Комментарий:__

------


__id:__ QAI2

__Приоритет:__ high

__Название:__ Получение объявления по его id

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
Отправить GET запрос https://qa-internship.avito.com/api/1/item/:id где :id это идентификатор объявления, полученный в предусловии



__Ожидаемый результат:__
Сервер пришлет ответ с:

HTTP Status: 200 OK

и телом в формате JSON:

```json
[
    {
        "createdAt": "2025-02-16 23:34:17.017088 +0300 +0300",
        "id": "a3daede9-85d2-419a-a92c-05a541144c6b",
        "name": "Приблуда",
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

Где:

1) id должно совпадать с отправленным id

2) name должны совпадать с отправленными в предусловии.

3) sellerID должны совпадать с отправленными в предусловии.

4) statistics должна совпадать со статистикой, заданной при создании объявления.

5) Т.к. в описании сервиса сказано, что id объявлений уникален, в массиве не должно быть больше одного объекта.

__Статус прохождения:__

1) PASSED

2) FAILED

3) PASSED

4) PASSED

5) PASSED


__Bug report:__
BR1

__Комментарий:__

-----


__id:__ QAI3

__Приоритет:__ high

__Название:__ Получить все объявления по идентификатору продавца

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
```

1) В ответе должны быть объявления, созданные в предусловии, т.е. с такими как у созданных id, name, price, statistics

2) sellerId во всех полученных объектах должен совпадать с sellerID из запроса

__Статус прохождения:__

1) FAILED

2) PASSED

__Bug report:__
BR2

__Комментарий:__

-----


__id:__ QAI4

__Приоритет:__ high

__Название:__ Получить статистику по айтем id

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

1) так как id объявлений должны быть уникальны, в массиве должен быть один объект

2) данные в объекте должны совпадать с данными статистики объявления из предусловия


__Статус прохождения:__

1) PASSED

2) FAILED

__Bug report:__
BR3


__Комментарий:__

-----


## Негативные тест-кейсы

__id:__ QAI5

__Приоритет:__ medium

__Название:__ Создание объявления без поля name

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

__Статус прохождения:__
FAILED

__Bug report:__
BR4

__Комментарий:__

-----

__id:__ QAI6

__Приоритет:__ medium

__Название:__ Создание объявления без поля price

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

__Статус прохождения:__
FAILED

__Bug report:__
BR5

-----

__id:__ QAI7

__Приоритет:__ medium

__Название:__ Создание объявления без поля SellerId

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

__Статус прохождения:__
FAILED

__Bug report:__
BR6


-----


__id:__ QAI8

__Приоритет:__ medium

__Название:__ Создание объявления c текстовым price

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

__Статус прохождения:__
PASSED

__Bug report:__


__Комментарий:__

-----
