# AWS and Remedy Integration
In the following tutorial I am going to describe the step by step required to integrate aws cloudwatch with Remedy Helix ITSM. Event though it could be the same process to integrate with any other exsposed web services, during this tutorial we will share the use of SOAP web services, which could be the midleware between AWS and Remedy Helix. The set of aws service that will be part of this integration are: cloudwatch alarm, SNS,Lambda, IAM, DynamoDB, Cloud9 & EC2

![Architecture](https://github.com/leosolano/aws_remedy/blob/main/img/img1.png)

# Step 1. Create an EC2 instance t2.micro and install stress tool 
As you might now cloudwath have the features of cloud alarm, but the intention here is to create a t2.micro aws linux 2 ami with Public IP enabled in order to access it via SSH and install the stress tool. 

1. login to the EC2 instance: ssh -i "key-pair" ec2-user@public_ip
2. Enable EPEL repo : "sudo amazon-linux-extras install epel -y"
3. Install Stress : "sudo yum install stress -y"

# Step 2. Create a cloudwatch alarm 
In this step the idea is to create a cloudwatch alarm based on the instance ID that you could capture from the EC2 console. Once you have the ID thats looks as i-4567sbsgsjsjsj, go to -->cloudwatch --> alarms -->create alarms --> select metric. At this poit you need to look inside the EC2 metrics related with the interested variable (CPUUtilization in our case). In the "conditions" section choice Greater or Greater/Equal, than and put the value in % for your alarm. In our exmaple it would be 90%, then hit "next". In the "Alarm state trigger" section choice *Create New Topic* and put the name of your new SNS Topic. If you didn't created a SNS topic preiovsly an email address would be required, but you could create an SNS topic previous to this step, and you can avoid to add an email address, to just subscribe a Lambda function as part of this topic. 

# Step 3. Create a Cloud9 Environment

            






