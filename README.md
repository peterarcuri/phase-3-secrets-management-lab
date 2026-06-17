# Phase 3 — Secrets Management Lab

A security-focused DevSecOps project demonstrating modern secret management practices for applications, CI/CD pipelines, and cloud environments.

This lab focuses on eliminating hardcoded credentials and implementing secure secret handling using environment variables, GitHub Actions Secrets, automated secret scanning, and AWS Secrets Manager integration.

---

# Objectives

This project is designed to strengthen practical DevSecOps skills in:

* Secure credential management
* Environment variable configuration
* GitHub Actions secret handling
* Secret scanning and detection
* AWS Secrets Manager integration
* Secure software delivery practices

---

# Features

## Current Features

* Environment variable configuration management
* `.env.example` template
* No hardcoded secrets
* AWS Secrets Manager integration demo
* GitHub Actions Secrets usage
* Automated secret scanning with Gitleaks
* Pytest test suite
* Ruff code quality validation

---

## Security Controls Demonstrated

### Secret Management

* Environment variables
* `.env.example` templates
* AWS Secrets Manager
* GitHub Actions Secrets

### Secret Detection

* Gitleaks repository scanning
* Commit history scanning
* Pull request scanning

### Secure Development Practices

* No hardcoded credentials
* Least privilege principles
* Secure configuration management
* Separation of code and secrets

---

# Project Structure

```text
phase-3-secrets-management-lab/
├── .github/
│   └── workflows/
│       └── secrets-security.yml
├── app/
│   ├── __init__.py
│   ├── aws_secrets_demo.py
│   └── config.py
├── docs/
│   ├── aws-secrets-manager-demo.md
│   └── secret-handling.md
├── sample-output/
│   ├── aws-secrets-demo-output.txt
│   └── config-demo-output.txt
├── screenshots/
├── tests/
│   └── test_config.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

---

# Technologies Used

* Python 3.13
* Pytest
* Ruff
* GitHub Actions
* Gitleaks
* AWS Secrets Manager
* Boto3
* Python Dotenv

---

# Installation

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

# Configuration

Create a local `.env` file:

```env
APP_NAME=phase-3-secrets-management-lab
ENVIRONMENT=development
AWS_REGION=us-east-1
AWS_SECRET_NAME=my-demo-secret
```

Important:

* Never commit `.env`
* Commit only `.env.example`
* Store production secrets in a secure secrets manager

---

# Running Tests

```bash
python -m pytest -v
```

---

# Running Ruff

```bash
ruff check .
```

---

# Running the AWS Secrets Manager Demo

```bash
python -m app.aws_secrets_demo
```

If AWS credentials are not configured, the application handles the condition safely without exposing sensitive information.

---

# GitHub Actions Security Pipeline

The GitHub Actions workflow performs:

* Ruff linting
* Pytest execution
* GitHub Actions secret validation
* Gitleaks secret scanning

Workflow file:

```text
.github/workflows/secrets-security.yml
```

---

# Documentation

Additional project documentation:

```text
docs/secret-handling.md
docs/aws-secrets-manager-demo.md
```

---

# Screenshots

## Project Structure

Shows the overall repository layout including application code, tests, documentation, GitHub Actions workflow, and secret management configuration.

![Project Structure](screenshots/project-structure-secrets-management.png)

---

## Configuration Loading Demonstration

Displays the application successfully loading configuration values from environment variables.

![Configuration Demo](screenshots/config-demo-secrets-management.png)

---

## Successful Pytest Execution

Demonstrates successful execution of the automated configuration test suite.

![Pytest Success](screenshots/pytest-success-secrets-management.png)

---

## Ruff Code Quality Validation

Shows Ruff validating code quality, formatting, and import organization.

![Ruff Success](screenshots/ruff-success-secrets-management.png)

---

## AWS Secrets Manager Integration Demo

Demonstrates the AWS Secrets Manager integration workflow and secure handling of missing credentials or secret retrieval.

![AWS Secrets Manager Demo](screenshots/aws-secrets-demo.png)

---

## GitHub Actions Security Pipeline Success

Displays successful execution of the GitHub Actions security workflow.

![GitHub Actions Success](screenshots/github-actions-success-secrets-management.png)

---

## Gitleaks Secret Scanning

Demonstrates automated secret scanning and validation using Gitleaks.

![Gitleaks Scan](screenshots/gitleaks-scan-secrets-management.png)

---

# Skills Demonstrated

* DevSecOps
* Secret Management
* Cloud Security
* AWS Security
* CI/CD Security
* Security Automation
* GitHub Actions
* Python Development
* Secure Configuration Management
* Secure Software Delivery

---

# Disclaimer

This project is intended for educational and portfolio purposes.

Do not store production credentials in source code repositories. Always use dedicated secret management solutions and follow organizational security policies.
