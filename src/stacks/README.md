# AWS CDK Stacks: BaseStack and GitHubOIDCStack

This documentation details the structure and functionality of two pivotal stacks within our AWS CDK TypeScript project: `BaseStack` and `GitHubOIDCStack`. These stacks lay the groundwork for deploying AWS resources with specific configurations and capabilities, tailored to different deployment stages and integration with GitHub Actions for CI/CD processes.

## BaseStack

The `BaseStack` serves as a foundational stack that you can use to start instantiation your custom and cdk-lib constructs.

### Properties

- `environment`: Optional. Specifies the deployment stage (e.g., `dev`, `test`, `staging`, `production`). It's crucial for tailoring the stack configuration to the target environment.

### Example Usage

```python
import os

import aws_cdk as cdk
from stacks.base_stack import BaseStack

# Inherit environment variables from npm run commands (displayed in .projen/tasks.json)
environment = os.environ.get("ENVIRONMENT", "dev")
aws_environment = cdk.Environment(account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION"))

# Instantiate the CDK app
app = cdk.App()

BaseStack(app, f"BaseStack-{environment}", env=aws_environment)
```

## GitHubOIDCStack

The GitHubOIDCStack is designed to facilitate secure CI/CD workflows by integrating AWS resources with GitHub Actions via OpenID Connect (OIDC). This allows for a more secure and streamlined deployment process directly from GitHub Actions.

### Features

- GitHub Actions OIDC Provider: Sets up the OIDC provider for GitHub Actions within the AWS account, enabling trust relationships between GitHub and AWS.
- GitHub Deploy Role: Creates an IAM role with AdministratorAccess managed policy. This role is assumable by GitHub Actions workflows, granting them the permissions needed to deploy resources.

### Configuration

The stack automatically retrieves GitHub repository details (owner and repository name) using a helper function, ensuring that the OIDC provider and IAM roles are correctly configured for the specific GitHub repository.

### Example Usage

```python
import os

import aws_cdk as cdk
from stacks.github_oidc_stack import GitHubOIDCStack

# Inherit environment variables from npm run commands (displayed in .projen/tasks.json)
environment = os.environ.get("ENVIRONMENT", "dev")
aws_environment = cdk.Environment(account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION"))

# Instantiate the CDK app
app = cdk.App()

GitHubOIDCStack(app, f"GitHubOIDCStack-{environment}", env=aws_environment)
```
