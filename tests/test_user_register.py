from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
import pytest
import allure


@allure.epic("Create user cases")
class TestUserRegister(BaseCase):
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user", data=data)
        assert response.status_code == 200, f"Unexpected status code {response.status_code}"
        Assertions.assert_code_status(response, 200)
        print(response.content)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = "cinkotov@example.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user", data=data)

        print(response.status_code)
        print(response.content)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists",\
            f"Unexpected response content {response.content}"

    def test_create_user_without_at(self):
        email = "cinkotovexample.com"
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user", data=data)

        print(response.status_code)
        print(response.content)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format",\
            f"Unexpected response content {response.content}"

    def test_create_user_with_short_name(self):
        data = self.prepare_registration_data(username="a")
        response = MyRequests.post("/user", data=data)

        print(response.status_code)
        print(response.content)
        Assertions.assert_code_status(response, 200)

    def test_create_user_with_long_name(self):
        username = "abcdefgehjabcdefgehjabcdefgehjabcdefgehja" \
                   "bcdefgehjabcdefgehjabcdefgehjabcdefgehjabcdefgehjab" \
                   "cdefgehjabcdefgehjabcdefgehjabcdefgehjabcdefgehjabcdef" \
                   "gehjabcdefgehjabcdefgehjabcdefgehjabcdefgehjabcdefgehja" \
                   "bcdefgehjabcdefgehjabcdefgehjabcdefgehjabcdefgehjabcdef" \
                   "gehjabcdefgehjabcdefgehjabcdefgehjabcdefgehj"
        data = self.prepare_registration_data(username=username)
        response = MyRequests.post("/user", data=data)

        print(response.status_code)
        print(response.content)
        Assertions.assert_code_status(response, 200)


    parameters_empty = [("cinkotov@examples.com", ""), ("", "learnqa")]

    @pytest.mark.parametrize('condition', parameters_empty)
    def test_register_user_with_field_missing(self, condition):
        data = self.prepare_registration_data(email=condition[0], username=condition[1])
        response = MyRequests.post("/user", data=data)

        print(response.status_code)
        print(response.content)
        Assertions.assert_code_status(response, 400)
        assert "field is too short" in response.content.decode("utf-8"), f"Unexpected response content {response.content}"









