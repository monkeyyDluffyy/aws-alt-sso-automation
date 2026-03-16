import yaml

from aws.sso_permissions import list_permission_sets
from aws.iam_roles import create_saml_provider, create_role
from aws.assignments import assign_group
from ui.create_external_app import create_external_app

def load_config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

def main():

    config = load_config()

    instance_arn = config["sso_instance_arn"]

    permission_sets = list_permission_sets(instance_arn)

    permission_set_arn = permission_sets[0]

    create_external_app(
        config["aws_console_url"],
        config["aws_username"],
        config["aws_password"],
        config["new_application_name"]
    )

    saml_metadata = "<xml>metadata</xml>"

    provider_arn = create_saml_provider(
        saml_metadata,
        config["saml_provider_name"]
    )

    create_role(
        config["role_name"],
        provider_arn
    )

    assign_group(
        instance_arn,
        permission_set_arn,
        "example-group-id",
        config["target_account_id"]
    )

if __name__ == "__main__":
    main()
