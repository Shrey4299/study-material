import requests
import json

# Define the URL and headers
url = 'https://www.instagram.com/graphql/query'
headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'datr=C3uzZjgSCQRyBRnledVH3Muj; ig_did=D202F041-A68D-4400-9870-890B39112B28; ps_l=1; ps_n=1; mid=Zs3cNwAEAAGyx9095Mrdyxq0O_Ye; ig_nrcb=1; csrftoken=Y65MwbuS1Zt7D76QMoMITXYXI26YP7sc; ds_user_id=15206397937; sessionid=15206397937%3AgG50q0P32dzEnv%3A17%3AAYeKkSRQNZEGCbXI35zLrH4lw9EHlwG6_8EACGdM_Q; shbid="4524\05415206397937\0541756303336:01f7698d0c65c34b470d67f789ed2a7d5a5f3ab70c411c52ba6db54bcf57464eb2e79c2a"; shbts="1724767336\05415206397937\0541756303336:01f7f9a7892cdba3ab2cf97ff69747a34743e20fd8660e3e5152a8453f8c47739435d255"; wd=1030x966; rur="CCO\05415206397937\0541756303394:01f71bbe77bb0ee5b54a6e361305bff82cc10fdefd9dcae74e6d5a08470bb01bb01e772f"; csrftoken=Y65MwbuS1Zt7D76QMoMITXYXI26YP7sc; ds_user_id=15206397937; rur="CCO\05415206397937\0541756304435:01f761e0e7527e8742ed4a6bb9abcde9b146b39d4b217b7c1a0a5548e8332ebdce66cb5b"',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/__shrey._7/following/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.155", "Google Chrome";v="124.0.6367.155", "Not-A.Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': 'Linux',
    'sec-ch-ua-platform-version': '6.8.0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-bloks-version-id': '6e3feacb109d958e99ad4cbea28c4dc16cbc29f315c4a77ef807950cbaf7c355',
    'x-csrftoken': 'Y65MwbuS1Zt7D76QMoMITXYXI26YP7sc',
    'x-fb-friendly-name': 'usePolarisRefetchFollowingListQuery',
    'x-fb-lsd': '8PmtEA6aGv1E5o-4vYInZe',
    'x-ig-app-id': '936619743392459',
}

# Define the base payload
payload_base = {
    'av': '17841415298120799',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': '28',
    '__hs': '19962.HYP:instagram_web_pkg.2.1..0.1',
    'dpr': '1',
    '__ccg': 'UNKNOWN',
    '__rev': '1015998859',
    '__s': 'qqi0kq:9t5egi:2mmfor',
    '__hsi': '7407819315220492319',
    '__dyn': '7xeUjG1mxu1syaxG4Vp41twpUnwgU7SbzEdF8aUco2qwJyEiw9-1DwUx60p-0LVE4W0om78c87m0yE462mcw5Mx62G5UswoEcE7O2l0Fwqo31w9a9wtUd8-U2exi4UaEW2G0AEco4i5o2eUlwhEe88o5i7U1mVEbUGdwtUd-2u2J08O321LwTwKG1pg2fwxyo6O1FwlEcUed6goK2OubxKi2qiUqwm9EO6UaU4W',
    '__csr': 'gacLfMH5hYp4EBkyNa8PqvXszOmlfvO9UxtHn9JTitdGIJrAy4KWRtGGmOp5ilTDIQyCWBjBUQLVkiLCBRiH-8BF94HKh4x2A42AzajAWiCO12GBHAAVaLCGcKiqlaGLiyp4Gh8-4euil12iKXVbjG4EWq00jaS486y0y8CO0amOkiEgxdto5m09JxK1YwHV3lgdS0NEggjSczorgSFSGw5rIB1Ih408JaGwba3W16AsE1DK1G-3e08vz5wnVU0LBwyDgCywnopAkmeQAmtQ_ig6d5O0To4NUhyoue78dCEghUIgc4h6444N81kE2wwVc4kgvjhqa7UqwDyZ0Uix1ghwn8pxmexm0_Q1fwiE2cV8563O0sG0nngfokJADgCl0FGBwbtBK2B0r82nxWmm0pd04XxSu8DK2rDg2cw1hG2bg1zA0FE0ckU4W0cKAg4K08hx11e0jaE2Uwdd0DBio0oHwJUc8',
    '__comet_req': '7',
    'fb_dtsg': 'NAcNwRCyD2yoms0H6SZcwq4O91b78XWdpf6j7cgDOoPKvDfw5oO80Kg:17864329786054772:1724767331',
    'jazoest': '26197',
    'lsd': '8PmtEA6aGv1E5o-4vYInZe',
    '__spin_r': '1015998859',
    '__spin_b': 'trunk',
    '__spin_t': '1724767339',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'usePolarisRefetchFollowingListQuery',
    'variables': '{"after":"{AFTER_VALUE}","before":null,"count":20,"first":10,"last":null,"query":"","userID":"15206397937"}',
    'server_timestamps': 'true',
    'doc_id': '8572502889430836',
}

# Prepare to collect usernames
usernames = []

# Iterate over the desired range for 'after' values
for after_value in range(2, 1400, 20):
    payload = payload_base.copy()
    payload['variables'] = payload['variables'].replace('{AFTER_VALUE}', str(after_value))
    
    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code == 200:
        data = response.json()
        edges = data.get('data', {}).get('xdt_api__v1__friendships__following__connection', {}).get('edges', [])
        for edge in edges:
            username = edge.get('node', {}).get('username')
            if username:
                usernames.append(username)
    else:
        print(f"Request failed with status code {response.status_code}")

# Save usernames to a JSON file
with open('usernames.json', 'w') as f:
    json.dump(usernames, f, indent=4)

print("Usernames have been saved to usernames.json")
