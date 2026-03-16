from aws.sso_permissions import list_permission_sets
from aws.iam_roles import create_saml_provider
from aws.assignments import assign_group
from ui.create_external_app import create_external_app


INSTANCE_ARN = "arn:aws:sso:::instance/ssoins-123"
ACCOUNT_ID = "111111111111"
ROLE_NAME = "ExternalSSORole"


def main():

    print("Fetching permission sets")

    permission_sets = list_permission_sets(INSTANCE_ARN)

    print(permission_sets)

    print("Creating External AWS App")

    create_external_app(
        username="admin",
        password="password",
        app_name="External-SSO-App"
    )

    print("Creating IAM role and IdP")

    create_saml_provider(
        ACCOUNT_ID,
        saml_metadata="<xml>",
        role_name=ROLE_NAME
    )

    print("Assigning group")

    assign_group(
        INSTANCE_ARN,
        permission_sets[0],
        principal_id="group-id",
        account_id=ACCOUNT_ID
    )


if __name__ == "__main__":
    main()
