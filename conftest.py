import pytest

import sender


@pytest.fixture
def item_body():
    return {
        "sellerID": 252677,
        "name": "Приблуда",
        "price": 255,
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12,
        },
    }


@pytest.fixture
def new_item_id(item_body):
    return sender.post_new_item(item_body).json().get('status').split()[-1]

second_new_item_id = new_item_id
