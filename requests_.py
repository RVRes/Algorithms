import requests

r = requests.get('http://example.com')  # simple get query
print(r)
print(r.headers)
print(r.text)


url = 'http://example.com'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=par)  # put parameters to query
print(r.url)  # url address with query params


url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies)  # send formed cookies to server
print(r.text)

print(r.cookies['example_cookie_name'])  # using cookies received from server
