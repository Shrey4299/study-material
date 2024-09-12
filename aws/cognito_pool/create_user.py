import boto3


# Configuration function for company-specific AWS Cognito settings
from aws.aws_key import get_company_config
from helper import get_cognito_client


# Function to create and return a Cognito client
# Function to create and return a Cognito client



# Function to create a new user in the specified Cognito User Pool
def create_cognito_user(
    company: str, username: str, temporary_password: str, email: str, role: str
):
    client = get_cognito_client(company)
    user_pool_id = get_company_config(company).get("cognito_user_pool_id")

    response = client.admin_create_user(
        UserPoolId=user_pool_id,
        Username=username,
        UserAttributes=[
            {"Name": "email", "Value": email},
            {"Name": "email_verified", "Value": "true"},
            {"Name": "custom:role", "Value": role},
        ],
        TemporaryPassword=temporary_password,
        MessageAction="SUPPRESS",  # This suppresses the sending of a welcome email
    )

    return response


# Example usage
if __name__ == "__main__":
    company_name = "your_company_name"  # Replace with your company name
    new_username = "new_username"  # Replace with the new user's username
    new_temp_password = "Temp@1234"  # Replace with a temporary password
    new_email = "user@example.com"  # Replace with the new user's email
    new_role = "SP"  # Replace with the role, e.g., "SP"

    response = create_cognito_user(
        company_name, new_username, new_temp_password, new_email, new_role
    )
    print("New user created:", response)
