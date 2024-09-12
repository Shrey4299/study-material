import boto3
from aws_key import get_company_config


def get_cognito_client():
    config = get_company_config()
    return boto3.client(
        "cognito-idp"
    )
