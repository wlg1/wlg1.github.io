# Does stopping instance stop charging all fees until it runs again?

When you stop an EC2 instance, you are essentially pausing the instance and the resources associated with it, such as the CPU, memory, and storage, are no longer allocated to the instance.

When an EC2 instance is stopped, you are still charged for any EBS (Elastic Block Store) volumes attached to the instance. You are also charged for any other associated resources, such as Elastic IP addresses, that are not associated with a running instance.

However, you are not charged for the instance hours while the instance is stopped. This means that you will not be charged for the compute resources used by the instance, such as the CPU and memory, while the instance is stopped.

It's worth noting that if you have reserved instances or savings plans associated with the stopped instance, you may still be charged for those, depending on the terms of your reservation or plan.

When you start the instance again, you will be charged for the compute resources used by the instance, as well as any associated resources that are charged on an hourly basis.

In summary, stopping an EC2 instance can help you save money on compute resources, as you are not charged for the instance hours while it is stopped. However, you may still be charged for other associated resources that are not associated with a running instance.