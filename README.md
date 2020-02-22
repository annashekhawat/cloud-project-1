# cloud-project-1
Project 1 (using the AWS EC2, S3, API Gateway, Lambda Functions) for the CSCE 678 Distributed Systems and Cloud Computing course


Name: Anna Shekhawat

-------------------------------------------------------------------

UIN: 930001909

-------------------------------------------------------------------

Cloud Platform used: AWS

-------------------------------------------------------------------

URL of AWS Lambda API Gateway: https://81944qf1v5.execute-api.us-east-2.amazonaws.com/v1/post-webpage?url=http://www.stackoverflow.com

The last portion of the URL is the argument where some website's URL needs to be passed as a query parameter. And the API is public.

-------------------------------------------------------------------

Command-line script: I have added a Python script that can be run to invoke the POST request on the API. Please provide the parameter URL as a command-line argument while runnning the Python script. Example:

$ python post-to-api.py http://www.stackoverflow.com

The above script is platform-independent. But I used the Operating System macOS High Sierra version 10.13.3

-------------------------------------------------------------------

S3 Bucket name: cloudproject-1

The instructor/TA has been granted permission on this bucket.

-------------------------------------------------------------------

Public DNS of EC2 instance: ec2-18-189-17-32.us-east-2.compute.amazonaws.com

The instructor/TA has been granted SSH permission. I have used Amazon Linux as server, so AWS CLI is already installed. After doing SSH, one needs to run the script like so:

$ python s3-monitor.py

The function in the script repeats itself every 60 seconds. So in every 60 seconds, it will go over the objects stored in the S3 bucket, and compute hash for any new html file and store it as an object in the same bucket.

-------------------------------------------------------------------
