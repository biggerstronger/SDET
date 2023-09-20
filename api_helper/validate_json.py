import requests

from data.json_schemas.create_estimate_json_schema import schema
from jsonschema import exceptions, validate


def validate_json(response: requests.Response) -> bool:
    try:
        validate(response, schema)
    except exceptions.ValidationError:
        return False
    return True
