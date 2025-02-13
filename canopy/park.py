import requests
from typing import List
import yaml

from canopy.models import environment as environment_model


class Park:
    """API for interacting with Park backend

    In the future, we should use the Park python api
    """

    def __init__(self, url: str):
        self.url = url

    def list_environments(self, namespace: str) -> List[str]:
        request_url = f"{self.url}/{namespace}/"
        response = requests.get(request_url)
        response.raise_for_status()
        data = response.json()
        return data["data"]["environments"]
    
    def list_checkpoints(self, namespace: str, environment: str) -> List[str]:
        request_url = f"{self.url}/{namespace}/{environment}/"
        response = requests.get(request_url)
        response.raise_for_status()
        data = response.json()
        return data["data"]["checkpoints"]

    def get_checkpoint(self, namespace: str, environment: str, checkpoint: str) -> environment_model.EnvironmentCheckpoint:
        request_url = f"{self.url}/{namespace}/{environment}/{checkpoint}"
        response = requests.get(request_url)
        response.raise_for_status()
        data = response.json()
        checkpoint_data = data["data"]["checkpoint_data"]
        checkpoint_dict = yaml.load(checkpoint_data, yaml.FullLoader)
        return environment_model.EnvironmentCheckpoint.model_validate(checkpoint_dict)
