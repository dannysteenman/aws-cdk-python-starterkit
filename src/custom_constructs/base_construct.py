import os

import aws_cdk as cdk
from constructs import Construct


class BaseConstruct(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.environment = os.environ.get("ENVIRONMENT", "dev")
        self.account = cdk.Stack.of(self).account
        self.region = cdk.Stack.of(self).region
