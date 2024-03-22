from aws_cdk import CfnOutput, Stack
from aws_cdk.aws_iam import ManagedPolicy
from aws_cdk_github_oidc import GithubActionsIdentityProvider, GithubActionsRole
from bin.git_helper import get_git_repo_details
from constructs import Construct


class GitHubOIDCStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        git_owner, repo_name = get_git_repo_details()

        provider = GithubActionsIdentityProvider.from_account(self, "GithubProvider")

        deploy_role = GithubActionsRole(
            self,
            "GitHubDeployRole",
            provider=provider,
            owner=git_owner,
            repo=repo_name,
            role_name="GitHubDeployRole",
            managed_policies=[ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")],
        )

        CfnOutput(self, "DeployRole", value=deploy_role.role_arn)
