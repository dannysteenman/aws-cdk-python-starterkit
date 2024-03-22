import aws_cdk as cdk
from constructs import Construct

# from custom_constructs.network_construct import NetworkConstruct


class BaseStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # ↓↓ instantiate your constructs here ↓↓
        # NetworkConstruct(self, "NetworkConstruct") # sample construct that creates a VPC
