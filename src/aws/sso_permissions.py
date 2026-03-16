from .boto_session import get_boto3_client
from utils.logger import get_logger

logger = get_logger()

def list_permission_sets(instance_arn):

    client = get_boto3_client("sso-admin")

    response = client.list_permission_sets(
        InstanceArn=instance_arn
    )

    permission_sets = response["PermissionSets"]

    logger.info(f"Found {len(permission_sets)} permission sets")

    return permission_sets
