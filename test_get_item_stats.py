import data
import sender


def test_get_created_item_stats(item_body, new_item_id):
    res = sender.get_item_stats(new_item_id)
    errors = []
    if not res.status_code == 200:
        errors.append('Статус не 200')

    res_body = res.json()
    if not len(res_body) == 1:
        errors.append("В ответе в массиве не один объект")

    res_stats = res_body[0]
    if not len(res_stats) == 3:
        errors.append('Количество ключей в статистике не 3')
    if not {
        'likes',
        'viewCount',
        'contacts',
    }.issubset(res_stats.keys()):
        errors.append(
            'В объекте ответа не хватает одного из ключей likes viewCount contacts'
        )

    if not (res_stats['likes'] == item_body['statistics']['likes']):
        errors.append(
            'В статистике полученной по item_id отличается количество likes от созданного объявления'
        )
    if not (res_stats['viewCount'] == item_body['statistics']['viewCount']):
        errors.append(
            'В статистике полученной по item_id отличается количество viewCount от созданного объявления'
        )
    if not (res_stats['contacts'] == item_body['statistics']['contacts']):
        errors.append(
            'В статистике полученной по item_id отличается количество contacts от созданного объявления'
        )
    assert not errors, "Возникли ошибки: {}".format("; ".join(errors))
