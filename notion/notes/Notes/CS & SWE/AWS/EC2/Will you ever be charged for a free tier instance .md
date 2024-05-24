# Will you ever be charged for a free tier instance such as t2.micro?

A t2.micro instance is part of the AWS Free Tier and provides a limited amount of usage for free each month. You can use one t2.micro instance continuously for up to 750 hours per month for free, for the first 12 months after you create your AWS account.

After the free tier period ends or if you exceed the free tier usage limits, you will be charged at the regular on-demand rates for the usage of the t2.micro instance.

It's important to note that while the t2.micro instance type is eligible for the free tier, other associated resources, such as Elastic IP addresses, data transfer, and EBS volumes, may not be eligible for the free tier and may incur charges.

It's also important to monitor your AWS usage closely and check your bill regularly to avoid unexpected charges. You can set up billing alerts and usage limits to help you manage your costs and stay within the free tier limits.

In summary, you will not be charged for a t2.micro instance that is within the free tier usage limits. However, you may be charged for associated resources or if you exceed the free tier limits.

---

Q: Will those hours count when the t2.micro is stopped?

No, the free tier hours for a t2.micro instance will not count when the instance is stopped.

When you stop a t2.micro instance, you are not charged for the instance hours while it is stopped, regardless of whether the instance is within the free tier usage limits or not. The free tier usage for a t2.micro instance is based on the number of instance hours that the instance is running, and the free tier benefits do not apply when the instance is stopped.

So if you have a t2.micro instance that is part of the free tier, you can stop and start it multiple times without incurring any charges for the instance hours while it is stopped. However, you should still monitor any associated resources such as EBS volumes, data transfer, or Elastic IP addresses, as these may still incur charges even when the instance is stopped.