from projen import github
from projen.awscdk import AwsCdkPythonApp

from src.bin.env_helper import cdk_action_task

project = AwsCdkPythonApp(
    author_email="danny@towardsthecloud.com",
    author_name="Danny Steenman",
    cdk_version="2.133.0",
    cdk_version_pinning=True,
    module_name="src",
    name="aws-cdk-python-starterkit",
    description="Create and deploy an AWS CDK app on your AWS account in less than 5 minutes using GitHub actions!",
    version="0.1.0",
    github_options={
        "pull_request_lint": False,
    },
    poetry=True,
    git_ignore_options={
        "ignore_patterns": [
            "__pycache__",
            "__pycache__/",
            ".python-version",
            "!.eslintrc.js",
            ".cache",
            ".coverage.*",
            ".coverage",
            ".DS_Store",
            ".env",
            ".mypy_cache",
            ".pytest_cache",
            ".Python",
            ".venv/",
            ".vscode",
            "*.js",
            "*.log",
            "*.manifest",
            "*.pyc",
            "*.spec",
            "*.zip",
            "**/cdk-test-report.xml",
            "*node_modules*",
            "build/",
            "coverage/",
            "dist/",
            "downloads/",
            "env/",
            "ENV/",
            "htmlcov/",
            "sdist/",
            "var/",
            "venv/",
        ],
    },
)

# Define the AWS Region for the CDK app
project.tasks.add_environment("CDK_DEFAULT_REGION", "us-east-1")

# Define the target AWS accounts for the different environments
target_accounts = {
    "dev": "987654321012",
    "test": "123456789012",
    "staging": None,
    "production": None,
}

# Loop through each environment in target_accounts
for env, account in target_accounts.items():
    if account:  # Check if account is not None
        # Adds customized projen tasks for executing cdk actions for each environment
        cdk_action_task(
            project,
            {
                "CDK_DEFAULT_ACCOUNT": account,
                "ENVIRONMENT": env,
            },
        )

project.synth()

gh = github.GitHub(project)
