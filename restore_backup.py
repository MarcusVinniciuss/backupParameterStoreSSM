import boto3
from csv import reader

client = boto3.client('ssm')

AWS_REGION =  "us-east-1"

ssm_client = boto3.client("ssm", region_name=AWS_REGION)

with open('params.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_params = list(csv_reader)

    list_params.remove(['Count', 'ParameterName', 'ParameterValue'])

    for item in list_params:
        print(item)
        new_string_parameter = ssm_client.put_parameter(
            Name= item[1],
            Value=item[2],
            Type='String',
            Overwrite=True,
            Tier='Standard',
            DataType='text')

        print("Created parameters")
