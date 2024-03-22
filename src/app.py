import os

import aws_cdk as cdk
from stacks.github_oidc_stack import GitHubOIDCStack

# Inherit environment variables from npm run commands (displayed in .projen/tasks.json)
environment = os.environ.get("ENVIRONMENT", "dev")
aws_environment = cdk.Environment(account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION"))

# Instantiate the CDK app
app = cdk.App()

# Add GitHub OpenID Connect support and create an IAM role for GitHub
GitHubOIDCStack(app, f"GitHubOIDCStack-{environment}", env=aws_environment)

# Tag all resources in CloudFormation with the environment name
cdk.Tags.of(app).add("Environment", environment)

# Synthesize the CDK app
app.synth()
