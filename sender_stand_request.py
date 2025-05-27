import configuration
import data
import requests

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                                  json=body,
                                  headers=data.headers)

def post_new_client_kit(kit_body, authToken):
    current_headers = data.headers.copy()
    current_headers["Authorization"] = "Bearer " + authToken
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=current_headers)