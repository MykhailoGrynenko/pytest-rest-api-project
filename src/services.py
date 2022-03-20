import json
import os
import logging

import requests


# print(os.environ["BASE_URL"])
BASE_URL = 'http://localhost:8000/api/v1/'
# url = os.environ['BASE_URL']
# print(url)


class ApiService:

    def __init__(self):
        self.base_url = BASE_URL

    @staticmethod
    def _get(url, token):
        response = requests.get(url, headers={'Authorization': f'token {token}'})
        logging.info(f'Sending a Get request to the url: {url} , with the token: {token}')
        return response

    @staticmethod
    def _post(url, payload):
        response = requests.post(url, data=json.dumps(payload), headers={"content-type": "application/json"})
        logging.info(f'Sending a Post request to the url: {url} , with the payload: {payload}')
        return response

    def _put(self, url, payload):
        pass

    def _patch(self, url, payload):
        pass


class UserApiService(ApiService):
    REGISTRATION_URL = 'dj-rest-auth/registration/'
    LOGIN_URL = 'dj-rest-auth/login/'
    GET_USER_DATA = 'dj-rest-auth/user/'

    def register(self, username, password):
        url = f'{self.base_url}{self.REGISTRATION_URL}'
        payload = {'username': username, 'password1': password, 'password2': password}
        logging.info(f'Trying to register: "username": {username}, "password": {password}')
        response = self._post(url, payload)
        logging.info(f"Request {response.request.url} \n {response.request.body}")
        logging.info(f"Response status code:{response.status_code}; body:{response.text}")
        return response

    def login(self, username, password):
        url = f'{self.base_url}{self.LOGIN_URL}'
        payload = {'username': username, 'password': password, 'password2': password}
        logging.info(f'Trying to login: "username": {username}, "password": {password}')
        response = self._post(url, payload)
        logging.info(f"Request {response.request.url} \n {response.request.body}")
        logging.info(f"Response status code:{response.status_code}; body:{response.text}")
        return response

    def get_user_data(self, username, password):
        url = f'{self.base_url}{self.GET_USER_DATA}'
        login_response = self.login(username, password)
        token = login_response.json()['key']
        response = self._get(url, token)
        logging.info(f"Request {response.request.url} \n {response.request.body}")
        logging.info(f"Response status code:{response.status_code}; body:{response.text}")
        return response
