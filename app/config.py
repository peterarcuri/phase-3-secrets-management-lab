"""
Configuration loader for the Secrets Management Lab.

This module demonstrates secure handling of configuration by 
reading sensitive values from the environment variables instead
of hardcoding them in source code
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

# Load variables from local .env file if present.
# In production or CI/CD, environment variables should be
# supplied externally (e.g., GitHub Actions Secrets).
load_dotenv()


@dataclass(frozen=True)
class Config:
    """Application configuration"""

    app_name: str
    environment: str
    aws_region: str
    aws_secret_name: str
    github_token: str | None


def get_config() -> Config:
    """
    Build and return application configuration from 
    environment variables
    """
    return Config(
        app_name=os.getenv(
            "APP_NAME",
            "phase-3-secrets-management-lab",
        ),
        environment=os.getenv(
            "ENVIRONMENT",
            "development",
        ),
        aws_region=os.getenv(
            "AWS_REGION",
            "us-east-1",
        ),
        aws_secret_name=os.getenv(
            "AWS_SECRET_NAME",
            "",
        ),
        github_token=os.getenv(
            "GITHUB_TOKEN",
        ),
    )

if __name__ == "__main__":
    config = get_config()

    print("Configuration loaded successfully") 
    print(f"Application: {config.app_name}")
    print(f"Environment: {config.environment}")
    print(f"AWS Region: {config.aws_region}")

    if config.aws_secret_name:
        print("AWS Secret Name: configured")
    else:
        print("AWS Secret Name: not configured")

    print(
        "GitHub Token: configured"
        if config.github_token
        else "GitHub Token: not configured"
    )

