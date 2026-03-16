import boto3


def list_permission_sets(instance_arn):
    client = boto3.client("sso-admin")

    response = client.list_permission_sets(
        InstanceArn=instance_arn
    )

    return response["PermissionSets"]


def describe_permission_set(instance_arn, permission_set_arn):
    client = boto3.client("sso-admin")

    response = client.describe_permission_set(
        InstanceArn=instance_arn,
        PermissionSetArn=permission_set_arn
    )

    return response["PermissionSet"]
