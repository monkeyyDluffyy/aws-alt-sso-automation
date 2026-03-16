import boto3
import json


def create_saml_provider(account_id, saml_metadata, role_name):

    iam = boto3.client("iam")

    response = iam.create_saml_provider(
        Name="ExternalSSOProvider",
        SAMLMetadataDocument=saml_metadata
    )

    provider_arn = response["SAMLProviderArn"]

    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Federated": provider_arn},
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
        Description="Role for external SSO access"
    )

    print(f"Role {role_name} created in account {account_id}")
