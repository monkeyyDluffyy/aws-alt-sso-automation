import boto3


def assign_group(
    instance_arn,
    permission_set_arn,
    principal_id,
    account_id
):

    client = boto3.client("sso-admin")

    response = client.create_account_assignment(
        InstanceArn=instance_arn,
        TargetId=account_id,
        TargetType="AWS_ACCOUNT",
        PermissionSetArn=permission_set_arn,
        PrincipalType="GROUP",
        PrincipalId=principal_id
    )

    return response
