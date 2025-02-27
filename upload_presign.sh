#!/bin/bash

#assign arguments to variables 
file=$1
bucket=$2
expiration=$3

#upload file to bucket
aws s3 cp "$file" "s3://$bucket/" --acl private || { echo "Upload failed"; exit 1; }

#generate and display presigned url 
aws s3 presign "s3://$bucket/$file" --expires-in "$expiration"
