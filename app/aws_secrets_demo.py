"""
AWS Secrets Manager demonstration

This example retrieves a secret from AWS Secret Manager
without exposing secret values in source code.

Requires:
    pip install boto3

Environment variables:
    AWS_REGION
    AWS_SECRET_NAME

AWS credentials should be supplied securely through:
- AWS CLI configuration
- IAM roles
- Environment variables
-GitHub ACtions Secrets

"""

from __future__ import annotations

import json

import boto3
from botocore.exceptions import ClientError

from config import get_config


def get_secret() -> str | None:

    """
    Retrieve a secret value from AWS Secrets Manager.

    Returns:
        Secret string or None if unavailable.
    """

    config = get_config()

    if not config.aws_secret_name:
        print("AWS_SECRET_NAME is not configured.")
        return None
    
    client = boto3.client(
        "secretsmanager",
        region_name=config.aws_region,
    )

    try:
        response = client.get_secret_value(
            SecretId=config.aws_secret_name,
        )

        return response.get("SecretString")
    
    except ClientError as exc:
        print(f"Unable to retrieve secret: {exc}")
        return None
    


def demo() -> None:
    """
    Demonstrate retreiving a secret without exposing
    sensitive values
    """

    secret = get_secret()

    if secret is None:
        print("No Secret retrieved.")
        return
    
    try:
        parsed = json.loads(secret)

        print("Secret retrieved successfully.")
        print("Available keys:")

        for key in parsed:
            print(f" - {key}")

    except json.JSONDecodeError:
        print("Secret retrieved successfully.")
        print(
            "Value received but intentionally not displayed "
            "to avoid exposing sensetive information."
        )


if __name__ == "__main__":
    demo()

