import boto3
from aws.aws_key import get_company_config


# Function to create and return a Cognito client
def get_cognito_client(company: str):
    config = get_company_config(company)
    return boto3.client(
        "cognito-idp",
        region_name=config.get("cognito_region"),
        aws_access_key_id=config.get("aws_access_key"),
        aws_secret_access_key=config.get("aws_secret_access_key"),
    )


# Function to find a user by email and return their username
def get_user_by_email(company: str, email: str):
    client = get_cognito_client(company)
    user_pool_id = get_company_config(company).get("cognito_user_pool_id")

    response = client.list_users(UserPoolId=user_pool_id, Filter=f'email="{email}"')

    users = response.get("Users", [])
    if users:
        return users[0][
            "Username"
        ]  # Assuming the email is unique and returning the first match
    return None


# Function to delete a user in the specified Cognito User Pool
def delete_cognito_user(company: str, username: str):
    client = get_cognito_client(company)
    user_pool_id = get_company_config(company).get("cognito_user_pool_id")

    response = client.admin_delete_user(UserPoolId=user_pool_id, Username=username)

    return response


# Example usage
if __name__ == "__main__":
    company_name = "your_company_name"  # Replace with your company name
    user_email = "user@example.com"  # Replace with the user's email

    # Find the user by email
    username = get_user_by_email(company_name, user_email)

    if username:
        # Delete the user
        response = delete_cognito_user(company_name, username)
        print(f"User '{username}' with email '{user_email}' has been deleted.")
    else:
        print(f"No user found with email '{user_email}'.")
