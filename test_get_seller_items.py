import data
import sender


def test_get_seller_items(item_body, new_item_id, second_new_item_id):
    res = sender.get_seller_items(item_body['sellerID'])
    errors = []
    if not res.status_code == 200:
        errors.append('Статус не 200')

    res_body = res.json()
    if not len(res_body) >= 2:
        errors.append('объявлений у продавца должно быть больше либо равно 2')

    if not all(
        map(lambda x: x['sellerId'] == item_body['sellerID'], res_body)
    ):  # у всех объявлений правильный sellerId
        errors.append('Не у все объявлений sellerId продавца')
    # Найдем в ответе новые объявления по их ид
    if not new_item_id in list(
        map(lambda x: x['id'], res_body)
    ): errors.append( f'В объявлениях продавца не нашли по id нового объявления с id={new_item_id}')
    if not second_new_item_id in list(
        map(lambda x: x['id'], res_body)
    ): errors.append(f'В объявлениях продавца не нашли по id нового объявления с id={second_new_item_id}')

    assert not errors, "Возникли ошибки: {}".format("; ".join(errors))
