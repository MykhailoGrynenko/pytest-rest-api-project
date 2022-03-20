import json
import allure


@allure.step
def test_register(user_api_service, fake):
    fake_username, fake_password = fake.user_name(), fake.password()
    response = user_api_service.register(fake_username, fake_password)
    assert response.status_code == 201
    assert len(response.json()["key"]) > 0
    assert fake_username == json.loads(response.request.body)['username']
    assert fake_password == json.loads(response.request.body)['password1']
    assert fake_password == json.loads(response.request.body)['password2']
