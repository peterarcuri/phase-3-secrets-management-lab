
# AWS Secrets Manager Demonstration

## Overview

This project includes a demonstration of retrieving secrets from AWS Secrets Manager using Python and Boto3.

The objective is to show how applications can securely access sensitive information without storing credentials directly within source code.

---

## Architecture

```text
Developer
    |
    v
Application
    |
    v
AWS SDK (Boto3)
    |
    v
AWS Secrets Manager
    |
    v
Encrypted Secret
```

The application requests a secret through the AWS SDK.

AWS Secrets Manager returns the encrypted secret value after validating permissions through AWS Identity and Access Management (IAM).

---

## Prerequisites

Before running the demonstration:

### Install Dependencies

```bash
pip install boto3 python-dotenv
```

### Configure AWS Credentials

AWS credentials can be configured using:

```bash
aws configure
```

Example:

```text
AWS Access Key ID
AWS Secret Access Key
Default Region
```

Credentials should never be committed to Git repositories.

---

## Example Secret

Example JSON secret stored in AWS Secrets Manager:

```json
{
  "username": "application-user",
  "password": "secure-password",
  "api_key": "example-api-key"
}
```

This example is for demonstration purposes only.

---

## Environment Variables

The application reads configuration from environment variables:

```env
AWS_REGION=us-east-1
AWS_SECRET_NAME=my-demo-secret
```

These variables may be supplied through:

* Local `.env`
* GitHub Actions Secrets
* Container runtime variables
* Cloud workload configuration

---

## Running the Demo

Execute the application:

```bash
python app/aws_secrets_demo.py
```

Expected output:

```text
Secret retrieved successfully.
Available keys:
 - username
 - password
 - api_key
```

The secret values themselves are intentionally not displayed.

---

## IAM Permissions

The application requires permission to retrieve secrets.

Example IAM policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": "*"
    }
  ]
}
```

For production environments, access should be restricted to specific secret ARNs.

---

## Security Benefits

AWS Secrets Manager provides:

* Encrypted secret storage
* Fine-grained IAM controls
* Automatic rotation support
* Audit logging through CloudTrail
* Centralized credential management

---

## DevSecOps Relevance

This demonstration reflects real-world cloud security practices commonly used in:

* DevSecOps engineering
* Platform engineering
* Cloud security
* Site Reliability Engineering (SRE)
* Security automation

Using a dedicated secret management platform significantly reduces the risk of credential exposure and supports secure software delivery pipelines.
