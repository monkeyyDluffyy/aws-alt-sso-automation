import boto3


def get_boto_session(profile=None, region="us-east-1"):
    if profile:
        session = boto3.Session(profile_name=profile, region_name=region)
    else:
        session = boto3.Session(region_name=region)
    return session


def get_client(service, profile=None):
    session = get_boto_session(profile)
    return session.client(service)
