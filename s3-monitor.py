import json
import boto3
import hashlib
import threading
import time

def monitor_s3():
    # TODO implement
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('cloudproject-1')
    dic = {}
    for obj in bucket.objects.all():
        file_name = obj.key
        if(file_name[-3:] == "tml"):
            if(file_name[:-5] not in dic):
                dic[file_name[:-5]] = 1
            else:
                dic[file_name[:-5]] += 1
        else:
            if(file_name[:-69] not in dic):
                dic[file_name[:-69]] = 1
            else:
                dic[file_name[:-69]] += 1
    for obj in bucket.objects.all():
        # open and read file
        file_name = obj.key
        if(file_name[-3:] == "tml"):
            if(dic[file_name[:-5]] is 2):
                continue
        else:
            continue
        file_obj = obj.get()
        file_content = file_obj["Body"].read()
        
        # generate hash
        s = hashlib.sha256(file_content)
        hex_s = s.hexdigest()
        
        # generate the new object to be stored
        new_file_name = file_name[:-5] + "_" + hex_s + ".txt"
        with open("/tmp/" + new_file_name, "w") as text_file:
            text_file.write(hex_s)
        
        # store the new object
        s3_client = boto3.client("s3")
        s3_client.upload_file("/tmp/"+ new_file_name, "cloudproject-1", new_file_name)
    threading.Timer(60, monitor_s3).start()

monitor_s3()
