# Run app in EC2

[https://github.com/PradipNichite/Youtube-Tutorials/blob/main/streamlit_gpt3_ec2/commands.txt](https://github.com/PradipNichite/Youtube-Tutorials/blob/main/streamlit_gpt3_ec2/commands.txt)

1. On EC2 page, click Launch EC2 instance
1.1. t2.micro (free)
1.2. save new key pair .pem
1.3. security group (allow traffic)
1.4. configure storage
2. under instances, click on it and click on connect
2.1. copy ssh command into git bash
ssh -i "instance.pem" [ec2-user@ec2-44-222-74-75.compute-1.amazonaws.com](mailto:ec2-user@ec2-44-222-74-75.compute-1.amazonaws.com)
3. in EC2 instance, create virtual env
python -m venv [name]
source [name]/bin/activate
4. copy files into venv
scp -i /path/to/key.pem /path/to/local/file [ec2-user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com](mailto:ec2-user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com):/path/to/remote/directory/
5. Run streamlit app in background
    
    pip install -r requirements.txt
    nohup streamlit [app.py](http://app.py/) &
    
6. in instance, go to security groups, edit inbound rules, add rules to allow traffic on the port that the app is running on (the port number depends on the app). choose 'anywhere’
7. click on external url (not local) to access app