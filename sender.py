import requests

import config
import data


def post_new_item(body):
    return requests.post(
        config.BASE_URL + config.CREATE_ITEM_PATH,
        json=body,
        headers=data.headers,
    )


def get_item(id):
    return requests.get(
        config.BASE_URL + config.GET_ITEM_PATH + id,
        headers=data.headers,
    )


def get_item_stats(id):
    return requests.get(
        config.BASE_URL + config.GET_ITEM_STATS_PATH + id,
        headers=data.headers,
    )


def get_seller_items(seller_id):
    return requests.get(
        config.BASE_URL
        + config.GET_SELLER_ITEMS_PATH.format(seller_id=seller_id),
        headers=data.headers
    )
