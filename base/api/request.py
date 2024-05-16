import gzip
import shutil
import requests
from base.datasource import _redis
from base.api.url import login
from base.entity.token import Token
from base.entity.config import Config
from base.api.data_to_class import json_to_class
from base.enums import *
from base.utils.string import generate_random_string


class Request:

    @staticmethod
    def __save_token__(token: Token):
        _redis.put_key(token_enums, token.to_dict(), ex=token.expires_in - 100)

    @staticmethod
    def __get_token__() -> Token:
        token = _redis.get_key(token_enums)
        if token is None:
            config = json_to_class(_redis.get_key(config_enums), Config)
            _ = requests.post(login, json={
                "grant_type": "refresh_token",
                "client_id": config.client_id,
                "client_secret": config.client_secret,
                "refresh_token": config.refresh_token
                }).json()
            token = json_to_class(_, Token)
            Request.__save_token__(token)
        return json_to_class(_redis.get_key(token_enums), Token)

    @staticmethod
    def __get_headers__():
        token = Request.__get_token__()
        config = json_to_class(_redis.get_key(config_enums), Config)
        return {
            "Authorization": f"Bearer {token.access_token}",
            "Amazon-Advertising-API-ClientId": config.client_id,
            "Amazon-Advertising-API-Scope": str(_redis.get_key(scope_id_enums))
            }

    @staticmethod
    def post(url: str, params: dict = None, data: dict = None, json: dict = None, headers: dict = None):
        header = Request.__get_headers__()
        if headers is not None:
            header.update(headers)
        return requests.post(url, json=json, data=data, headers=header, params=params).json()

    @staticmethod
    def get(url: str, params: dict = None, headers: dict = None):
        header = Request.__get_headers__()
        if headers is not None:
            header.update(headers)
        return requests.get(url, params=params, headers=header).json()

    @staticmethod
    def download(url: str):
        response = requests.get(url, stream=True)
        file_name = generate_random_string(16)
        with open(f'{file_name}.gz', 'wb') as f:
            shutil.copyfileobj(response.raw, f)
        with gzip.open(f'{file_name}.gz', 'rb') as f_in:
            with open(f'{file_name}.json', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        with open(f'{file_name}.json', 'r') as f:
            content = f.read()
        return content
