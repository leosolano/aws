# AWS and Remedy Integration
In the following tutorial I am going to describe the step by step required to integrate aws cloudwatch with Remedy Helix ITSM. Event though it could be the same process to integrate with any other exsposed web services, during this tutorial we will share the use of SOAP web services, which could be the midleware between AWS and Remedy Helix. The set of aws service that will be part of this integration are: cloudwatch alarm, SNS,Lambda, IAM, DynamoDB, Cloud9 & EC2

![Architecture](https://github.com/leosolano/aws_remedy/blob/main/img/img1.png)

# Step 1. Create an EC2 instance t2.micro and install stress tool 
As you might now cloudwath have the features of cloud alarm, but the intention here is to create a t2.micro aws linux 2 ami with Public IP enabled in order to access it via SSH and install the stress tool. 

# **login to the EC2 instance

sudo amazon-linux-extras install epel -y


