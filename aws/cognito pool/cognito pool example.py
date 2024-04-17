import boto3

# Initialize the Cognito client
client = boto3.client('cognito-idp', region_name='your_region')

# Example operations with User Pools API

# SignUp: Register a new user
response = client.sign_up(
    ClientId='your_client_id',
    Username='new_user@example.com',
    Password='password',
    UserAttributes=[
        {
            'Name': 'email',
            'Value': 'new_user@example.com'
        }
    ]
)
print("Sign up response:", response)

# SignIn: User sign in
response = client.initiate_auth(
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': 'new_user@example.com',
        'PASSWORD': 'password'
    },
    ClientId='your_client_id'
)
print("Sign in response:", response)

# ListUsers: List users in a user pool
response = client.list_users(
    UserPoolId='your_user_pool_id'
)
print("List users response:", response)

# Example operations with Identity Pools API

# GetId: Get identity ID for a new identity
response = client.get_id(
    AccountId='your_account_id',
    IdentityPoolId='your_identity_pool_id',
    Logins={
        'cognito-idp.your_region.amazonaws.com/your_user_pool_id': 'user_token'
    }
)
print("Get identity ID response:", response)

# GetOpenIdToken: Get OpenID Connect token for an identity
response = client.get_open_id_token(
    IdentityId=response['IdentityId']
)
print("Get OpenID token response:", response)

# GetCredentialsForIdentity: Get temporary AWS credentials for an identity
response = client.get_credentials_for_identity(
    IdentityId=response['IdentityId']
)
print("Get credentials response:", response)
