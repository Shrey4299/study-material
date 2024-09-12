import boto3
from aws.aws_key import get_company_config
from helper import get_cognito_client


# Function to create and return a Cognito client



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


# Function to update user attributes in the specified Cognito User Pool
def update_cognito_user(company: str, username: str, role: str):
    client = get_cognito_client(company)
    user_pool_id = get_company_config(company).get("cognito_user_pool_id")

    response = client.admin_update_user_attributes(
        UserPoolId=user_pool_id,
        Username=username,
        UserAttributes=[
            {"Name": "custom:role", "Value": role},
        ],
    )

    return response


# Example usage
if __name__ == "__main__":
    company_name = "your_company_name"  # Replace with your company name
    user_email = "user@example.com"  # Replace with the user's email
    new_role = "new_role_value"  # Replace with the new role, e.g., "Admin"

    # Find the user by email
    username = get_user_by_email(company_name, user_email)

    if username:
        # Update the user's role
        response = update_cognito_user(company_name, username, new_role)
        print(f"User '{username}' updated with new role '{new_role}':", response)
    else:
        print(f"No user found with email '{user_email}'.")
