# backupParameterStoreSSM

This project is a simple lambda function that create AWS ParameterStore backup, sending the file backup to s3 bucket.

## Setup to run project
To run this project, using Python:

```
cd lambda
sudo pip3 install requests -t .
sudo pip3 install pytz -t .
sudo zip -r lambda_function.zip .
sudo rm -rf -v !("lambda_function.py"|"lambda_function.zip")
``` 

After run this commands:

- Create a lambda function on aws and update the code using "Upload from .zip file",  do upload the file "lambda_function.zip" and your code will be ok.

- Go to IAM and create two policies ("ListParams" and "S3AllowPull"), to create the policies use the json template in this folder 'lambda/Policies/'.

- After created the policies, go to IAM > Roles > your-lambda-role. Go to "Add permissions" and attach the policies that you created.

- Now, create a bucket s3 with Versioning enabled, copy the arn bucket and paste on your policy 'S3AllowPull'.



## How to create pparameters using backup file

- First, configure your credentials aws who you that will be using to create parameters.
- Now, download the backup file and paste local path into your code, on csv parameters.


Done!

