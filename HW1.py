from typing import List, Dict
from secrets import token_urlsafe


def filter_products(products: List[Dict[str, int]], max_price: int) -> List[str]:

    return [product['product'] for product in products if product['price'] <= max_price]


def test_no_matching_products():
    products = [{'product': 'bread', 'price': 30}, {'product': 'milk', 'price': 40}]
    max_price = 10
    assert filter_products(products, max_price) == []


def test_all_products_match():
    products = [{'product': 'bread', 'price': 25}, {'product': 'milk', 'price': 15}]
    max_price = 30
    assert filter_products(products, max_price) == ['bread', 'milk']


def test_partial_products_match():
    products = [{'product': 'bread', 'price': 25}, {'product': 'milk', 'price': 40}]
    max_price = 30
    assert filter_products(products, max_price) == ['bread']


def test_empty_product_list():
    products = []
    max_price = 50
    assert filter_products(products, max_price) == []


def generate_random_string(length: int = 20) -> str:


    random_string = token_urlsafe(length)
    return random_string + "abcde"


def test_generate_random_string():
    assert len(generate_random_string()) == 25
    assert generate_random_string(10).endswith("abcde")
    assert generate_random_string(15).endswith("abcde")
    assert generate_random_string(5) == "abcde"
    assert generate_random_string(0) == "abcde"

import pytest



def test_no_matching_products():
    products = [{'product': 'bread', 'price': 30}, {'product': 'milk', 'price': 40}]
    max_price = 10
    assert filter_products(products, max_price) == []


def test_all_products_match():
    products = [{'product': 'bread', 'price': 25}, {'product': 'milk', 'price': 15}]
    max_price = 30
    assert filter_products(products, max_price) == ['bread', 'milk']


def test_partial_products_match():
    products = [{'product': 'bread', 'price': 25}, {'product': 'milk', 'price': 40}]
    max_price = 30
    assert filter_products(products, max_price) == ['bread']


def test_empty_product_list():
    products = []
    max_price = 50
    assert filter_products(products, max_price) == []


def test_generate_random_string():
    assert len(generate_random_string()) == 25
    assert generate_random_string(10).endswith("abcde")
    assert generate_random_string(15).endswith("abcde")
    assert generate_random_string(5) == "abcde"
    assert generate_random_string(0) == "abcde"