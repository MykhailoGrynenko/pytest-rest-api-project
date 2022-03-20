import pytest
import logging
from faker import Faker

from src.services import UserApiService


@pytest.fixture(scope='session')
def fake():
    logging.info(f"A faker instance is returned")
    return Faker()


@pytest.fixture(scope='session')
def fake_username(fake):
    return fake.user_name()


@pytest.fixture(scope='session')
def fake_password(fake):
    return fake.password()


@pytest.fixture(scope='session')
def user_api_service():
    logging.info('Creating an instance of UserApiService')
    return UserApiService()


@pytest.fixture(scope='session')
def register(user_api_service, fake_username, fake_password):
    logging.info(f'Registration is completed via fixture: "username": {fake_username}, "password": {fake_password}')
    return user_api_service.register(fake_username, fake_password)


@pytest.fixture(scope='session')
def login(user_api_service, fake_username, fake_password, register):
    logging.info(f'Login is completed via fixture: "username": {fake_username}, "password": {fake_password}')
    return user_api_service.login(fake_username, fake_password)
