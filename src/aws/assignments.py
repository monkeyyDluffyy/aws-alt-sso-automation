from .boto_session import get_boto3_client
from utils.logger import get_logger

logger = get_logger()

def assign_group(instance_arn, permission_set_arn, group_id, account_id):

    client = get_boto3_client("sso-admin")

    response = client.create_account_assignment(
        InstanceArn=instance_arn,
        TargetId=account_id,
        TargetType="AWS_ACCOUNT",
        PermissionSetArn=permission_set_arn,
        PrincipalType="GROUP",
        PrincipalId=group_id
    )

    logger.info("Group assigned successfully")

    return response
