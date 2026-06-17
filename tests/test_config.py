
"""
Tests for the configuration laoder.

These tests verify that configuration values are loaded from
environment vairables and that sensitive defaults are used when
variables are not defined
"""

from app.config import get_config


def test_default_configuration(monkeypatch):
    """Verify default values are used when environment variables are absent"""

    monkeypatch.delenv("APP_NAME", raising=False)
    monkeypatch.delenv("ENVIRONMENT", raising=False)
    monkeypatch.delenv("AWS_REGION", raising=False)
    monkeypatch.delenv("AWS_SECRET_NAME", raising=False)
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)

    config = get_config()

    assert config.app_name == "phase-3-secrets-management-lab"
    assert config.environment == "development"
    assert config.aws_region  == "us-east-1"
    assert config.aws_secret_name == ""
    assert config.github_token is None


def test_environment_overrides(monkeypatch):
    """Verify environment variables override defaults values."""

    monkeypatch.setenv("APP_NAME", "my-secure-app")
    monkeypatch.setenv("ENVIRONMENT", "production")
    monkeypatch.setenv("AWS_REGION", "us-west-2")
    monkeypatch.setenv("AWS_SECRET_NAME", "prod/database")
    monkeypatch.setenv("GITHUB_TOKEN", "placeholder-token")

    config = get_config()

    assert config.app_name == "my-secure-app"
    assert config.environment == "production"
    assert config.aws_region == "us-west-2"
    assert config.aws_secret_name ==  "prod/database"
    assert config.github_token == "placeholder-token"
