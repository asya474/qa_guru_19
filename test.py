import jsonschema
import pytest
import requests
from requests import Response

from utils import load_schema


def test_get_single_user_successfully():
    url = "https://reqres.in/api/users/2"
    schema = load_schema("json_schemes/get_single_user.json")

    result: Response = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)

def test_post_create_201_succesfully():
    url = "https://reqres.in/api/users"
    schema = load_schema("json_schemes/post_create.json")

    result: Response = requests.post(url)

    assert result.status_code == 201
    jsonschema.validate(result.json(), schema)

def test_put_update_200_succesfully():
    url = "https://reqres.in/api/users/2"
    schema = load_schema("json_schemes/put_update.json")

    result: Response = requests.put(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)

def test_delete_204_succesfully():
    url = "https://reqres.in/api/users/2"

    result: Response = requests.delete(url)

    assert result.status_code == 204



def test_404():
    pass

def test_400():
    pass

def test_json_scheme_one():
    pass

def test_json_scheme_two():
    pass

def test_json_scheme_three():
    pass

def test_json_scheme_four():
    pass

def test_json_scheme_five():
    pass

def test_with_answer():
    pass

def test_without_answer():
    pass
