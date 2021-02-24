# AWS and Remedy Integration
In the following tutorial I am going to describe the step by step required to integrate aws cloudwatch with Remedy Helix ITSM. Event though it could be the same process to integrate with any other exsposed web services, during this tutorial we will share the use of SOAP web services, which could be the midleware between AWS and Remedy Helix. The set of aws service that will be part of this integration are: cloudwatch alarm, SNS,Lambda, IAM, DynamoDB, Cloud9 & EC2

![Architecture](https://github.com/leosolano/aws_remedy/blob/main/img/img1.png)

# Step 1. Create an EC2 instance t2.micro and install stress tool 
As you might now cloudwath have the features of cloud alarm, but the intention here is to create a t2.micro aws linux 2 ami with Public IP enabled in order to access it via SSH and install the stress tool. 

1. login to the EC2 instance: ssh -i "key-pair" ec2-user@public_ip
2. Enable EPEL repo : "sudo amazon-linux-extras install epel -y"
3. Install Stress : "sudo yum install stress -y"

# Step 2. Create a cloudwatch alarm 
In this step the idea is to create a cloudwatch alarm based on the instance ID that you could capture from the EC2 console. Once you have the ID thats looks as i-4567sbsgsjsjsj, go to -->cloudwatch --> alarms -->create alarms --> select metric. At this point you need to look inside the EC2 metrics related with the interested variable (CPUUtilization in our case). In the "conditions" section choice Greater or Greater/Equal, than and put the value in % for your alarm. In our exmaple it would be 90%, then hit "next". In the "Alarm state trigger" section choice *Create New Topic* and put the name of your new SNS Topic. If you didn't created a SNS topic preiovsly an email address would be required, but you could create an SNS topic previous to this step, and you can avoid to add an email address, to just subscribe a Lambda function as part of this topic. 

# Step 3. Create a Cloud9 Environment
As part of the integration process it´ll be require to use some python libraries that are not present in Lamda by default, it is why you need to create a Cloud9 environment, wher you couls install the python modules that are not present in Lambda, as "zeep" library, required to make SOAP calls to the remedy web services. 
Go to Cloud9 Environment, and create the smaller instance you can four your project. Once you have your environment ready install the zeep package following the next comands: python -m pip install --target=./ zeep. If any other external library is required just go and use the following public post: https://aws.amazon.com/premiumsupport/knowledge-center/cloud9-deploy-lambda-external-libraries/

# Step 4. Create a DynamoDB Table (Optional)
For thos cases where the information that comes from the cloudwatch alarms is not enough to fill the form to pass the alarm to Helix, would be a good idea to create a DynamoDB table including some fields that could be linked with the AWS AccountID, as customer name, etc. In this case the table we created includes just the account ID and customer name fields, but account ID is the partition key in this DynamoDB table.



# Step 5. Create your Lambda code from Cloud9.
            






