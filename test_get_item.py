import data
import sender


def test_get_created_item(item_body, new_item_id):
    res = sender.get_item(new_item_id)
    errors = []
    if not res.status_code == 200:
        errors.append('Статус не 200')

    res_body = res.json()
    if not len(res_body) == 1:
        errors.append('В ответе не одно объявление')

    res_item = res_body[0]
    if not len(res_item) == 6:
        errors.append("количество полей в ответе не 6")
    if not {
        'id',
        'name',
        'price',
        'sellerId',
        'createdAt',
        'statistics',
    }.issubset(res_item.keys()):
        errors.append('В теле ответа нет одного из необходимых полей')

    else:
        if not (res_item['id'] == new_item_id):
            errors.append(
                'id полученного объявления не совпадает с id созданного'
            )
        if not (res_item['name'] == item_body['name']):
            errors.append(
                'name полученного объявления не совпадает с name созданного'
            )
        if not (res_item['price'] == item_body['price']):
            errors.append(
                'price полученного объявления не совпадает с price созданного'
            )
        if not (res_item['sellerId'] == item_body['sellerID']):
            errors.append(
                'sellerId полученного объявления не совпадает с sellerId созданного'
            )
        if not (res_item['statistics'] == item_body['statistics']):
            errors.append(
                'statistics полученного объявления не совпадает с statistics созданного'
            )
    assert not errors, "Возникли ошибки: {}".format("; ".join(errors))
