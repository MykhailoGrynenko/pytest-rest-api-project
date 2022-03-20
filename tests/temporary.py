# def test_login_valid_credentials(user_api_service, fake):
#     fake_username, fake_password = fake.user_name(), fake.password()
#     user_api_service.register(fake_username, fake_password)
#     response = user_api_service.login(fake_username, fake_password)
#     assert response.status_code == 200
#     assert len(response.json()['key']) > 0
#
#
# def test_login_invalid_username(user_api_service, fake):
#     fake_username, fake_password = fake.user_name(), fake.password()
#     wrong_username = fake_username + '_'
#     user_api_service.register(wrong_username, fake_password)
#     response = user_api_service.login(fake_username, fake_password)
#     assert response.status_code == 400
#
#
# def test_login_invalid_password(user_api_service, fake):
#     fake_username, fake_password = fake.user_name(), fake.password()
#     wrong_password = fake_password + '_'
#     user_api_service.register(fake_username, wrong_password)
#     response = user_api_service.login(fake_username, fake_password)
#     assert response.status_code == 400

# def test_get_user_data(user_api_service, fake):
#     fake_username, fake_password = fake.user_name(), fake.password()
#     user_api_service.register(fake_username, fake_password)
#     response = user_api_service.get_user_data(fake_username, fake_password)
#     assert response.status_code == 200
#     assert len(str(response.json()['pk'])) > 1
#     assert response.json()['username'] == fake_username







# [pytest]
# log_cli = 1
# log_cli_level = INFO
# log_cli_format = %(asctime)s [%(levelname)4s] %(message)s
# env =
#     BASE_URL=http://127.0.0.1:8000/api/v1




# def test_login_valid_credentials_a(login):
#     assert login.status_code == 200
#     assert len(login.json()['key']) > 0
#
#
# def test_login_valid_credentials_b(user_api_service, fake_username, fake_password, register):
#     response = user_api_service.login(fake_username, fake_password)
#     assert response.status_code == 200
#     assert len(response.json()['key']) > 0
#
#
# def test_login_valid_credentials_c(user_api_service, fake):
#     fake_username, fake_password = fake.user_name(), fake.password()
#     user_api_service.register(fake_username, fake_password)
#     response = user_api_service.login(fake_username, fake_password)
#     assert response.status_code == 200
#     assert len(response.json()['key']) > 0


# def test_register_valid_credentials(register, fake_username, fake_password):
#     assert register.status_code == 201
#     assert fake_username == json.loads(register.request.body)['username']
#     assert fake_password == json.loads(register.request.body)['password1']
#     assert fake_password == json.loads(register.request.body)['password2']
#     print(fake_username)
#     x = register.request.body
#     print(json.loads(x), type(json.loads(x)))
#     print(register.json(), type(register.json))
#     print(register.json()['key'], type(register.json()['key']))
#     user_id = register.json()['key']


# def test_login_valid_credentials(fake_username, fake_password, login):
#     assert login.status_code == 200
#     user_id = login.json()['key']
#     print(user_id)
#
#     # url5 = 'http://127.0.0.1:8000/api/v1/dj-rest-auth/user/'
#     # res5 = requests.get(url5, headers={'Authorization': f'token {user_id}'})
#     # print(res5)
#     # print(f'response {res5.json()}')
#
#     print(json.loads(login.request.body))
#     # x = json.loads(login.request.body)['id']
#     # print(x, type(x))
#     url = f'http://localhost:8000/api/v1/users/61'
#     res = requests.delete(url, headers={'Authorization': f'token {user_id}'})
#     print(res.status_code)