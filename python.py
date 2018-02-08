import boto3

more = nil
args = dict(Path=os.environ.get('SSM_PATH'), WithDecryption=True)
ssm = boto3.client('ssm')
parameters = []
while more != false:
    if more:
        args["NextToken"] = more        
    res = ssm.get_parameters_by_path(
        Path=os.environ.get('SSM_PATH'),
        WithDecryption=True
    )
    parameters.extend(res['Parameters'])
    more = res.get("NextToken", false)

for secret in parameters:
    os.environ[secret.get('Name').split('/')[-1]] = secret.get('Value')
