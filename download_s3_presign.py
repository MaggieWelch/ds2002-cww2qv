#!/usr/bin/env python3

import urllib.request
import boto3

#fetch and save a file from the internet using urllib

file_url = "https://www.adorama.com/alc/wp-content/uploads/2021/05/bird-wings-flying.gif"
file_name = "saved.gif"

try:
	urllib.request.urlretrieve(file_url, file_name)
except Exception as e:
	print("Failed down download file")
	exit()

#Upload file to S3
s3 = boto3.client("s3", region_name="us-east-1")
bucket = "ds2002-cww2qv"

try:
	s3.upload_file(file_name, bucket, file_name)
	print(" ")
	print(f"File uploaded to s3: {file_name}")
except Exception as e:
	print("S3 upload failed")
	exit()

#Generate presigned URL 
expiration_time = 3600

try:
	presigned_url = s3.generate_presigned_url(
		"get_object",
		Params={"Bucket": bucket, "Key": file_name},
		ExpiresIn=expiration_time
	)
	print("Presigned URL, valid for 1 hour:")
	print(" ") 
	print(f"{presigned_url}")
	print(" ")
except Exception as e:
	print("Failed to generate presigned URL")
	exit()
