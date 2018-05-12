import boto3, os
'''
    Sets your os environ variables to whatever is at the current SSM Path

    /bin/sh# SSM_PATH=/ python python.py

    will print out your current os environ variables based on whatever is at the root ssm path
'''

ssm = boto3.client('ssm')
paginator = ssm.get_paginator('get_parameters_by_path')
iterator = paginator.paginate(Path=os.environ.get('SSM_PATH'), WithDecryption=True)
params = []
for page in iterator:
    params.extend(page['Parameters'])
    for param in page.get('Parameters', []):
        os.environ[param.get('Name').split('/')[-1]] = param.get('Value')
print(os.environ)
