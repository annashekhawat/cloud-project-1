import json
import urllib.request
import boto3

def lambda_handler(event, context):
    urlstring = event["params"]["querystring"]["url"]
    urlstring_withoutslashes = urlstring.replace('/', '-')
    
    urllib.request.urlretrieve (urlstring, "/tmp/"+ urlstring_withoutslashes +".html")
    
    s3 = boto3.client("s3")
    s3.upload_file("/tmp/"+ urlstring_withoutslashes +".html", "cloudproject-1", urlstring_withoutslashes +".html")
    return urlstring

