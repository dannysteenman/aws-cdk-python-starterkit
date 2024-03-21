from projen import github
from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
    author_email="danny@towardsthecloud.com",
    author_name="Danny Steenman",
    cdk_version="2.133.0",
    cdk_version_pinning=True,
    module_name="aws_cdk_python_starterkit",
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

project.synth()

gh = github.GitHub(project)
