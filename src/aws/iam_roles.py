import json
from .boto_session import get_boto3_client
from utils.logger import get_logger

logger = get_logger()


def create_saml_provider(metadata_xml, provider_name):

    iam = get_boto3_client("iam")

    response = iam.create_saml_provider(
        Name=provider_name,
        SAMLMetadataDocument=metadata_xml
    )

    provider_arn = response["SAMLProviderArn"]

    logger.info(f"SAML Provider created: {provider_arn}")

    return provider_arn


def create_role(role_name, provider_arn):

    iam = get_boto3_client("iam")

    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Federated": provider_arn
                },
                "Action": "sts:AssumeRoleWithSAML",
                "Condition": {
                    "StringEquals": {
                        "SAML:aud": "https://signin.aws.amazon.com/saml"
                    }
                }
            }
        ]
    }

    iam.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy),
        Description="Role for External SSO"
    )

    logger.info(f"IAM Role created: {role_name}")
