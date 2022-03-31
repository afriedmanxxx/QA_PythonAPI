# QA_PythonAPI
Allure:
pytest --alluredir=test_results tests/test_user_auth.py
allure serve test_results

In order to run tests in different environments create variable ENV=prod (prod, dev) and add to the global variables list in bash-profile

DOCKER setup:
docker pull python
docker build -t pytest_runner .
docker run --rm --mount type=bind,src={path to framework},target=/tests_project/ pytest_runner

docker-compose up --build

