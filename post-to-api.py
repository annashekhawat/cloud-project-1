import requests
import sys

args_list = sys.argv
print(args_list)
url_of_the_webpage_to_store = args_list[1]

post_api_url = 'https://81944qf1v5.execute-api.us-east-2.amazonaws.com/v1/post-webpage?url=' + url_of_the_webpage_to_store
post_request_reponse = requests.post(post_api_url)

print("response:")
print(post_request_reponse)
print('headers:')
print(post_request_reponse.headers)
print('status code:')
print(post_request_reponse.status_code)