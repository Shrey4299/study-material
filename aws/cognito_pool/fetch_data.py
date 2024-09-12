import boto3


# Configuration function for company-specific AWS Cognito settings
from aws_key import get_company_config
from helper import get_cognito_client


# Function to list users in the specified Cognito User Pool
def list_cognito_users():
    # client = get_cognito_client()\
    client = boto3.client("cognito-idp")
    user_pool_id = get_company_config().get("cognito_user_pool_id")


    response = client.list_users(UserPoolId=user_pool_id)
    
    


    return response["Users"]


def filter_users_by_role(users, role_list):
    filtered_users = []
    for user in users:
        for attribute in user["Attributes"]:
            if (
                attribute["Name"] == "custom:role"
                and attribute["Value"] not in role_list
            ):
                filtered_users.append(user)
    return filtered_users


# Example usage
if __name__ == "__main__":
    users = list_cognito_users()
    # role_list = ["SP", "CM", "CL", "DM", "PROLL", "FIN", "FM"]

    # Filter users whose custom:role is "SP"
    # sp_users = filter_users_by_role(users, role_list)

    # Print the filtered user information
    for user in users:
        print(user)
