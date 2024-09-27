import requests

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/signup/birthday/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Xiaomi Redmi Note 11"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-asbd-id': '129477',
    'x-csrftoken': 'nJ0AZOCYo2lBMNHk3x6pKQNFa0wmbBXn',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1016696497',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'name': str(input('Username (username): '))
}

response = requests.post(
    'https://www.instagram.com/api/v1/web/accounts/username_suggestions/',
    headers=headers,
    data=data,
)

if 'suggestions' in response.text:
    print(response.json()['suggestions'])
else:
    print('BAD Username')
