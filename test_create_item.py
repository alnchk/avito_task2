import data
import sender


def test_create_correct_item(item_body):
    res = sender.post_new_item(item_body)
    errors = []
    if not res.status_code == 200:
        errors.append('Статус не 200')

    res_json = res.json()
    if not len(res_json) == 1:
        errors.append('В ответе не одно поле')

    status = res_json.get('status')
    if not isinstance(status, str):
        errors.append('status не строка')

    assert not errors, "Возникли ошибки: {}".format("; ".join(errors))

def negative_assert(bad_item):
    res = sender.post_new_item(bad_item)
    errors = []
    if not res.status_code == 400:
        errors.append('Статус не 400')

    res_body = res.json()
    if not 'status' in res_body:
        errors.append('В ответе нет поля status')
    elif not isinstance(res_body['status'], str):
        errors.append('status не строка')

    if not 'result' in res_body:
        errors.append('В ответе нет поля result')

    assert not errors, "Возникли ошибки: {}".format("; ".join(errors))


def test_create_item_with_text_price(item_body):
    bad_item = item_body.copy()
    bad_item['price'] = 'дорого'
    negative_assert(bad_item)


def test_create_item_without_seller(item_body):
    bad_item = item_body.copy()
    bad_item.pop('sellerID')
    negative_assert(bad_item)


def test_create_item_without_name(item_body):
    bad_item = item_body.copy()
    bad_item.pop('name')
    negative_assert(bad_item)

def test_create_item_without_price(item_body):
    bad_item = item_body.copy()
    bad_item.pop('price')
    negative_assert(bad_item)
