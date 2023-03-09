import pytest
import requests

# ДОБАВЬ ALLURE!!!


BASE_LINK = "https://restful-booker.herokuapp.com/"
TOKEN = 'ca42ddcb18303a4'
BOOKING_ID = ''


# базовый тест для проверки получения токена
# def est_get_api_token():
#    header = {'Content-Type': 'application/json'}
#    cred_json = {'username': 'admin', 'password': 'password123'}
#    res = requests.post(BASE_LINK + "auth", headers=header, json=cred_json)
#    assert res.status_code == 200
#    assert 'token' in res.json()
#    print(res.json())


# базовый тест для проверки доступности основного линка
def test_base_link():
    res = requests.get(BASE_LINK)
    assert res.status_code == 200, "NO ACCESS: " + str(res.status_code)


# базовый тест для проверки доступности сервиса
def test_health_check():
    res = requests.get('https://restful-booker.herokuapp.com/ping')
    assert res.status_code == 201, "Site is down" + str(res.status_code)


# тест на проверку бронирования (здесь надо подключить JSON-валидатор)
def test_create_booking():
    header = {'Content-Type': 'application/json'}
    booking_details = {
        "firstname": "Adilbek",
        "lastname": "Konysbek",
        "totalprice": 111,
        "depositpaid": 'true',
        "bookingdates":
            {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
        "additionalneeds": "Breakfast"
    }
    res = requests.post(BASE_LINK + 'booking', headers=header, json=booking_details)
    assert res.json()['booking']['firstname'] == 'Adilbek'
    assert res.json()['booking']['lastname'] == 'Konysbek'
    assert res.json()['booking']['totalprice'] == 111
    assert res.json()['booking']['depositpaid'] == True
    assert res.json()['booking']['bookingdates']['checkin'] == '2018-01-01'
    assert res.json()['booking']['bookingdates']['checkout'] == '2019-01-01'
    assert res.json()['booking']['additionalneeds'] == 'Breakfast'
    assert 'bookingid' in res.json()

@pytest.mark.parametrize('id', ['840'])
def test_get_bookings(id):
    res = requests.get(BASE_LINK + 'booking/' + id)
    expected_json = {
        'firstname': 'Bob',
        'lastname': 'Smith',
         'totalprice': 111,
         'depositpaid': True,
         'bookingdates':
             {
                 'checkin': '2018-01-01',
                 'checkout': '2019-01-01'
             },
         'additionalneeds': 'Breakfast'
    }

    assert res.json() == expected_json
