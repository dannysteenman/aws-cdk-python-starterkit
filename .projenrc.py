from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
    author_email="danny@towardsthecloud.com",
    author_name="Danny Steenman",
    cdk_version="2.1.0",
    module_name="aws_cdk_python_starterkit",
    name="aws-cdk-python-starterkit",
    version="0.1.0",
)

project.synth()