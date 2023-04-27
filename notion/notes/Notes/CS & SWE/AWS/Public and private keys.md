# Public and private keys

![Untitled](Public%20and%20private%20keys%20ed72fcf450d544939cb92ae1591f7c14/Untitled.png)

When you connect to an EC2 instance using SSH, the client software on your computer uses the public key to encrypt the data that is sent to the instance. The instance then uses its private key to decrypt the data.

This provides a secure way of authenticating and connecting to an EC2 instance, as the private key is kept on your local computer and is never transmitted over the network. The public key is shared with the EC2 instance, but because it is only used for encryption, it cannot be used to decrypt any data sent from the instance.