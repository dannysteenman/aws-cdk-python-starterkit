# AWS CDK Constructs: BaseConstruct and NetworkConstruct

This README provides a comprehensive guide to understanding and utilizing the `BaseConstruct` and `NetworkConstruct` within your AWS CDK project, emphasizing the importance of environment-aware configurations.

## BaseConstruct

The `BaseConstruct` serves as a foundational construct from which other constructs can inherit. It provides essential properties that are common across different environments, such as development (`dev`), testing (`test`), staging (`staging`), and production (`production`).

### Properties

- `environment`: Determines the environment context (`dev`, `test`, `staging`, `production`). Defaults to `dev` if not specified.
- `account`: The AWS account ID where resources will be deployed.
- `region`: The AWS region where resources will be deployed.

### Usage

When creating a new construct that requires environment-specific logic, you can extend `BaseConstruct` to inherit these properties. This approach streamlines the process of applying conditional logic based on the environment.

```python
from constructs import Construct
from .base_construct import BaseConstruct

class MyConstruct(BaseConstruct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        # Your construct logic here, with access to self.environment, self.account, self.region
```

## NetworkConstruct

The NetworkConstruct extends BaseConstruct and showcases how to leverage inherited properties to configure resources differently across environments. It focuses on deploying a Virtual Private Cloud (VPC) with environment-specific settings.

### Features

- VPC Configuration: Deploys a VPC with a varying number of NAT gateways and IP ranges based on the environment.
- S3 Flow Logs: Configures VPC Flow Logs, stored in an S3 bucket with environment-specific policies for object deletion and removal.

**Environment-Specific Logic**

- **IP Ranges**: Sets the VPC's CIDR block based on the environment:
  - dev: 172.16.0.0/16
  - test: 172.17.0.0/16
  - production: 172.18.0.0/16
- **NAT Gateways**: Deploys a single NAT gateway for non-production environments and three for production, optimizing cost and high availability.
- **S3 Bucket Policies**: For non-production environments, automatically enables object deletion and bucket removal upon stack deletion. Production environments use default settings for manual management.

Example to enable this construct in your stack:

```python
import aws_cdk as cdk
from constructs import Construct

from custom_constructs.network_construct import NetworkConstruct


class MyStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        NetworkConstruct(self, "NetworkConstruct")
```
