import allure
import requests
from lib.my_requests import MyRequests
from lib.assertions import Assertions
from lib.base_case import BaseCase
import pytest


class TestUserDelete:
    def test_delete_user_with_diff_id(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        #url = "https://playground.learnqa.ru/api/user/{id}"
        id = 2
        response = MyRequests.delete(url="/user/{id}", data=data)
        print(response.content)

    def test_positive_delete_user(self):
        pass
        #Create user
        #Authorize user
        # Delete user
        # Get data by user id and assert no data found

    def test_delete_diff_user(self):
        pass
        # auth user 1
        # Delete user 2
        # Assert no user 2 doesn't get deleted
