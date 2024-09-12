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


# Function to fetch user information using a token
def fetch_user_by_token(company: str, token: str):
    client = get_cognito_client(company)

    response = client.get_user(AccessToken=token)

    return response


# Example usage
if __name__ == "__main__":
    company_name = "your_company_name"  # Replace with your company name
    user_token = "user_token_here"  # Replace with the user's token (access or ID token)

    # Fetch user details using the token
    user_details = fetch_user_by_token(company_name, user_token)

    # Print the fetched user details
    print("User details fetched from Cognito:", user_details)
