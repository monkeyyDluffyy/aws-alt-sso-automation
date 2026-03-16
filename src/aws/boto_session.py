import boto3
import yaml

def load_config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

def get_boto3_client(service):
    config = load_config()
    return boto3.client(service, region_name=config["region"])
