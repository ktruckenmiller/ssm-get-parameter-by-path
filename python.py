ssm = boto3.client('ssm')
res = ssm.get_parameters_by_path(
    Path=os.environ.get('SSM_PATH'),
    WithDecryption=True
)
parameters = res['Parameters']

while res.get('NextToken'):
    res = ssm.get_parameters_by_path(
        Path=os.environ.get('SSM_PATH'),
        WithDecryption=True,
        NextToken=res.get('NextToken')
    )
    parameters.extend(res['Parameters'])
for secret in parameters:
    os.environ[secret.get('Name').split('/')[-1]] = secret.get('Value')
