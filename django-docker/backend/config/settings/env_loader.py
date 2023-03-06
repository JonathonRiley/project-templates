# import environ
import os
from os.path import join, dirname
from dotenv import load_dotenv

from django.core.exceptions import ImproperlyConfigured

class EnvLoader:
    def __init__(self, env_path:str) -> None:
        self.env_path = env_path
        self.load_env_reader()

    def load_env_reader(self) -> None:
        dotenv_path = join(dirname(__file__), self.env_path)
        if not os.path.exists(dotenv_path):
            error_msg = f'File not found: {dotenv_path}'
            raise FileNotFoundError(error_msg)
        load_dotenv(dotenv_path)

    def get_env_variable(self, var_name:str):
        var_value = os.environ.get(var_name)
        if not var_value:
            error_msg = f'Set the {var_name} environment variable'
            raise ImproperlyConfigured(error_msg)
        return var_value