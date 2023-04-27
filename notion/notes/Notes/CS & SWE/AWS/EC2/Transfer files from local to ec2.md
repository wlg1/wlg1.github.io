# Transfer files from local to ec2

Q: What is the scp command to transfer files from local to an EC2 instance?
The scp (secure copy) command is a Linux command that allows you to securely transfer files between a local machine and a remote machine. Here's an example scp command to transfer files from a local machine to an EC2 instance:

scp -i /path/to/key.pem /path/to/local/file [ec2-user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com](mailto:ec2-user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com):/path/to/remote/directory/

This command transfers the file located at /path/to/local/file on your local machine to the EC2 instance at the specified IP address (in this case [ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com](http://ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com/)) and saves it to the directory specified at /path/to/remote/directory/.

Here's a breakdown of the different parts of the command:

scp: the command itself

- i /path/to/key.pem: the path to the private key used to connect to the EC2 instance

/path/to/local/file: the path to the file you want to transfer from your local machine

[ec2-user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com](mailto:ec2-user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com): the username and IP address (or DNS name) of the EC2 instance you want to transfer the file to

:/path/to/remote/directory/: the path to the directory on the EC2 instance where you want to save the transferred file

Make sure to replace /path/to/key.pem, /path/to/local/file, [ec2-user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com](mailto:ec2-user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com), and /path/to/remote/directory/ with the appropriate values for your setup.

---

Q: How do we find  the username and IP address (or DNS name) of the EC2 instance you want to transfer the file to?

To transfer files to an EC2 instance using scp, you need to know the username and IP address (or DNS name) of the instance. Here are two methods to find this information:

AWS Management Console:
Log in to the AWS Management Console.
Open the EC2 dashboard.
Find the instance you want to transfer files to in the Instances tab.
Check the "Instance ID" column to find the instance's ID.
Check the "Public DNS (IPv4)" column to find the instance's public DNS name.
To find the username, check the "AMI ID" column and look up the default username for the operating system you are running on the instance.

AWS CLI:
Open the terminal or command prompt on your local machine.
Install the AWS CLI and configure it with your AWS credentials.
Run the following command to get a list of all your EC2 instances:

aws ec2 describe-instances
Look for the instance you want to transfer files to in the output and note its "InstanceId" value.
Run the following command to get the instance's public DNS name:
scss

aws ec2 describe-instances --instance-ids <instance_id> --query 'Reservations[0].Instances[0].PublicDnsName' --output text
Replace <instance_id> with the instance ID you noted earlier.

To find the username, you can use the same method as in the AWS Management Console method.