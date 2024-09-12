import requests
import json

# Instagram GraphQL URL
url = "https://www.instagram.com/graphql/query"

# Headers to be sent with each request
headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'datr=C3uzZjgSCQRyBRnledVH3Muj; ig_did=D202F041-A68D-4400-9870-890B39112B28; ps_l=1; ps_n=1; mid=Zs3cNwAEAAGyx9095Mrdyxq0O_Ye; ig_nrcb=1; csrftoken=Y65MwbuS1Zt7D76QMoMITXYXI26YP7sc; ds_user_id=15206397937; sessionid=15206397937%3AgG50q0P32dzEnv%3A17%3AAYeKkSRQNZEGCbXI35zLrH4lw9EHlwG6_8EACGdM_Q; shbid="4524\05415206397937\0541756303336:01f7698d0c65c34b470d67f789ed2a7d5a5f3ab70c411c52ba6db54bcf57464eb2e79c2a"; shbts="1724767336\05415206397937\0541756303336:01f7f9a7892cdba3ab2cf97ff69747a34743e20fd8660e3e5152a8453f8c47739435d255"; wd=699x966; rur="CCO\05415206397937\0541756307896:01f7f9905b7babc658c0aa9d86c2bbfa5947547bac6d69363e7558f7aa3115a8f1df342b"',  # Replace with your actual cookie data
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/__shrey._7/followers/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.155", "Google Chrome";v="124.0.6367.155", "Not-A.Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '"6.8.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-bloks-version-id': '6e3feacb109d958e99ad4cbea28c4dc16cbc29f315c4a77ef807950cbaf7c355',
    'x-csrftoken': 'your_csrf_token_here',  # Replace with your actual CSRF token
    'x-fb-friendly-name': 'usePolarisRefetchFollowersListQuery',
    'x-fb-lsd': 'your_fb_lsd_token_here',  # Replace with your actual FB LSD token
    'x-ig-app-id': '936619743392459',
}

# Initialize an empty list to store usernames
usernames = []
end_cursor = "QVFBYjlocW5hZk95a09VZHFpMV9ISkg4Y1ktMTZncHp4WmhVbjc1SkozUExNUEd0WnFJRmd6TUJDeWpKbmxTZy1hTk82alVRNzVpSUlhV1NSSmdORGtqSw"
has_next_page = True


# Loop to handle pagination
while has_next_page:
    # Construct the variables dictionary
    variables = {
        "after": end_cursor,
        "before": None,
        "count": 20,
        "first": 10,
        "last": None,
        "query": "",
        "userID": "15206397937"
    }

    # Convert variables to JSON string
    variables_json = json.dumps(variables)

    # Construct payload with the variables JSON
    payload = {
        'variables': variables_json,
        'fb_api_req_friendly_name': 'usePolarisRefetchFollowersListQuery',
        'doc_id': '7892969524119199',
    }

    # Send the request
    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()


        # Extract usernames from the current page
        edges = data.get("data", {}).get("xdt_api__v1__friendships__followers__connection", {}).get("edges", [])
        usernames.extend([edge["node"]["username"] for edge in edges])

        # Update pagination information
        page_info = data.get("data", {}).get("xdt_api__v1__friendships__followers__connection", {}).get("page_info", {})
        end_cursor = page_info.get("end_cursor")
        has_next_page = page_info.get("has_next_page", False)
    else:
        print(f"Request failed with status code {response.status_code}")
        break

# Save all usernames to a JSON file
with open('follower_list.json', 'w') as f:
    json.dump(usernames, f, indent=4)

print("Usernames have been saved to follower_list.json")
