import pytest
import requests

BASE_LINK = "https://restful-booker.herokuapp.com/"

# базовый тест для проверки доступности основного линка
def test_base_link():
    res = requests.get(BASE_LINK)
    assert res.status_code == 200, "NO ACCESS: " + res.status_code