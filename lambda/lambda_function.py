import boto3
import csv
import json


def get_parameters():
    #ssm = boto3.client('ssm')
    AWS_REGION = "us-east-1"

    ssm_client = boto3.client('ssm', region_name=AWS_REGION)
    paginator = ssm_client.get_paginator('describe_parameters')
    page_iterator = paginator.paginate().build_full_result()

    list1 = []
    count = 0

    for page in page_iterator['Parameters']:
        response = ssm_client.get_parameter(
            Name=page['Name'],
            WithDecryption=True
        )

        value = response['Parameter']['Value']

        parameter_name = page['Name']
        parameter_value = value

        count += 1
        
        values_param = f'{count} {parameter_name} {parameter_value}'

        test_split = values_param.split()

        list1.append(test_split)

        print(test_split)

    fields = ['Count','ParameterName', 'ParameterValue']
    filename = '/tmp/params.csv'

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(list1)
    print(list1)


def send_csv_s3():
    s3 = boto3.client('s3')
    bucket = 'parameters-bkp'
    s3.upload_file('/tmp/params.csv', bucket, 'params.csv')
    print('Arquivo enviado')


def lambda_handler(event, context):
    get_parameters()
    send_csv_s3()
    
    return {
        'statusCode': 200,
        'body': json.dumps("Teste ")
    }