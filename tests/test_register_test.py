# import requests
# import json
#
#
# def test_register_valid_credentials():
#     url = 'http://127.0.0.1:8000/api/v1/'
#     url2 = 'http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/'
#     payload = {'username': 'myname41', 'password1': 'qwerty54321', 'password2': 'qwerty54321'}
#     response = requests.post(url2, data=json.dumps(payload), headers={"content-type": "application/json"})
#     print(response, type(response))
#     print(response.request, type(response.request))
#     print(response.request.body, type(response.request.body))
#     x = response.request.body
#     print(json.loads(x), type(json.loads(x)))
#     print(f'response {response.json()}')
#     assert response.status_code == 201
#
#     url4 = 'http://127.0.0.1:8000/api/v1/dj-rest-auth/login/'
#     payload2 = {'username': 'myname25', 'password': 'qwerty54321'}
#     res4 = requests.post(url4, data=json.dumps(payload2), headers={"content-type": "application/json"})
#     print(res4)
#     print(f'response4 {res4.json()}')
#     # assert response.status_code == 201
#     url3 = 'http://127.0.0.1:8000/api/v1/users/'
#     res3 = requests.get(url3, params=payload2, headers={'Authorization': 'token 04a092a9b1d4138cdda224b9c5e7209144653907'})
#     print(res3)
#     print(f'response {res3.json()}')
#
#     url5 = 'http://127.0.0.1:8000/api/v1/dj-rest-auth/user/'
#     res5 = requests.get(url5, params=payload2, headers={'Authorization': 'token 04a092a9b1d4138cdda224b9c5e7209144653907'})
#     print(res5)
#     print(f'response {res5.json()}')
#
#     res5_2 = requests.get(url5, headers={'Authorization': 'token 04a092a9b1d4138cdda224b9c5e7209144653907'})
#     print(res5_2)
#     print(f'response {res5_2.json()}')
