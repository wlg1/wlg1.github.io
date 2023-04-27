# When running app, get: This site cannot be reached

Q: When launching a streamlit app on ec2, there is a network error. how does changing inbound rules in security groups solve this?

When launching a Streamlit app on EC2, a network error can occur if the security group associated with the instance does not allow incoming traffic on the port that the app is running on. By changing the inbound rules in the security group, you can allow incoming traffic on the required port and resolve the network error.

Here's how you can change the inbound rules in the security group to allow incoming traffic:

1. Open the EC2 dashboard in the AWS Management Console.
2. Click on the "Security Groups" link in the left-hand menu.
3. Find the security group associated with the EC2 instance that you are running the Streamlit app on, and click on the "Edit inbound rules" button.
4. Click on the "Add rule" button and select the protocol and port that the Streamlit app is running on. For example, if your Streamlit app is running on port 8501 using the HTTP protocol, you would select "HTTP" as the protocol and enter "8501" as the port range.
5. Save the changes to the security group.

By allowing incoming traffic on the required port, you are telling the security group to permit network traffic to reach the EC2 instance running the Streamlit app. This allows users to access the app from their web browsers, without encountering a network error.

It's important to note that allowing incoming traffic from the internet can pose a security risk, so make sure to only allow traffic on the ports that your application requires, and configure any additional security measures, such as firewalls or VPNs, as needed.

---

[data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)

Why 8501?

8501 is the default port used by Streamlit to serve web applications. When you run a Streamlit application using the **`streamlit run`** command, it starts a local web server that listens on port 8501 by default.

When you deploy a Streamlit app to an EC2 instance, you need to configure the security group associated with the instance to allow incoming traffic on the port that the Streamlit app is running on. By default, the Streamlit app will continue to use port 8501 when deployed on an EC2 instance, unless you specify a different port using the **`--server.port`** command-line argument when launching the app.

Therefore, when you configure the inbound rules in the security group associated with the EC2 instance, you need to allow incoming traffic on port 8501 to enable users to access the Streamlit app running on the instance.

It's worth noting that while 8501 is the default port used by Streamlit, you can configure it to use a different port if needed. To do this, you can specify the desired port using the **`--server.port`** command-line argument when launching the Streamlit app, and then configure the security group to allow incoming traffic on the specified port.

---

[data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)

How do we know which port to use?

The port number to use depends on the application or service you are running.

In general, well-known services such as HTTP (web server), SSH (secure shell), FTP (file transfer protocol), etc., use specific default port numbers. For example, HTTP typically uses port 80 or 443 (for HTTPS), SSH uses port 22, and FTP uses ports 20 and 21.

However, for custom applications or services, you may need to specify a port number to use. When developing or configuring an application, you should consult the documentation or configuration files to determine which port number the application or service is configured to use.

For example, in the case of a Streamlit app, the default port used is 8501, as mentioned in the Streamlit documentation. You can also specify a different port number using the **`--server.port`** command-line argument when launching the app.

Once you know the port number that the application or service is using, you can configure the inbound rules in the security group associated with the EC2 instance to allow incoming traffic on that port. It's important to ensure that you only allow incoming traffic on the required ports to minimize security risks.