from attr import field
import boto3
import csv

ssm = boto3.client('ssm')

AWS_REGION = "us-east-1"

ssm_client = boto3.client('ssm', region_name=AWS_REGION)

paginator = ssm_client.get_paginator('describe_parameters')

page_iterator = paginator.paginate().build_full_result()

for page in page_iterator['Parameters']:
    response = ssm_client.get_parameter(
        Name=page['Name'],
        WithDecryption=True
    )
    
    value = response['Parameter']['Value']
    
    parameter_name = page['Name']
    parameter_value = value
    
    filename = "parameter_bkp.csv"
    fields = ['Parameter', 'Value']
    rows = []
    
    print(f'{parameter_name} - {parameter_value}')

    
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        
        for key in parameter_name.keys():
            csvwriter.writerows((key,parameter_name[key])) 
