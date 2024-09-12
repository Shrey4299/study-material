def get_username_from_access_token(access_token: str):
    """
    It will return the username from the access token
    """

    return JWTBearer().verify_cognito_token(access_token)


def get_user_token_data(token_username: str) -> dict:
    """
    This function decodes and gets the user attributes from given username.
    :param token_username: user token
    :return: decoded token
    """
    client = boto3.client('cognito-idp', region_name=settings.COGNITO_AWS_REGION,
                          aws_access_key_id=settings.AWS_ACCESS_KEY,
                          aws_secret_access_key=settings.AWS_SECRETE_ACCESS_KEY)
    response = client.admin_get_user(
        UserPoolId=settings.COGNITO_USER_POOLID, Username=token_username)
    user_data = {}
    for obj in response["UserAttributes"]:
        user_data[obj["Name"]] = obj["Value"]
    return user_data