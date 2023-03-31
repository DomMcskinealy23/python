#!/usr/bin/python3

import boto3

client = boto3.client('sts')
identity = client.get_caller_identity()


http = (identity['ResponseMetadata']['HTTPStatusCode'])

if http == 200:
    print('well done congratultions your user id is' + identity['UserId'])
else:
    print('fuck off')