from requests import Response
import json

class Assertions:
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in Json format. Json text is {response.text}"

        assert name in response_as_dict, f"Response json doens't have any key {name}"
        assert response_as_dict[name] == expected_value, error_message



