# CAIS

We wanted to ask about buying compute from CAIS. Ideally, what this would look like is:

1. We pay some money (possibly paying for additional hardware).
2. We get a partition with preemptible GPUs on the CAIS cluster that we can freely run jobs on, including adding our own users.
2a. Other users would be able to use our lab’s GPUs while they would otherwise be idling, but we’d be able to interrupt these jobs.
2b. (Maybe?) Our lab would maybe be able to use general CAIS resources if they were idling, and likewise would be interrupted if someone requests the GPUs for an CAIS-approved project.
2c. This would be jobs on any project our lab is working on, rather than approved projects.
3. (Maybe it makes more sense to just have dedicated compute instead?)

We heard that working with individual groups to provide compute was that you would be interested in doing. Would something like this be possible?

<<<

At the moment we can offer either reserved nodes or higher priority for running jobs in the general compute pool shared with others. If you'd prefer preemptible GPUs, we could set up one or more nodes for you on this basis, but it would likely be a couple of weeks until our team has capacity to set this up for you. We would prefer not to make other GPUs preemptible across the cluster, as this could interfere with other researchers' jobs if they haven't been configured to be interruptible.

Let me know which of these three options (those below or preemptible GPUs) would work best 

Reserved partition

Benefit:
dedicated use of reserved GPUs, which are not available to other users

Minimum booking:
8 GPUs, 48 hours

Pricing

GPUs:
$1.55 per GPU-hour where GPU is reserved

For example, if a user reserves 8 GPUs for 48 hours (even if they
are not actually using the GPUs for 100% of this time), this would cost $576

Storage:
$0.0004 per GB-hour of total storage for users that have access to the reserved node

Data egress:
$0.0085 per GB

Shared partition - priority boost

Benefit:
Users access the same pool of shared resources as currently, but have first priority in running jobs (a regular free user has a fair share of 1 in SLURM, while paid users have a fair share of 2)

Minimum booking:
1 user for 1 month

Other conditions:
The GPUs are still shared and priority will be partly linked to other factors such as job size. Therefore, there could still be some wait time to run jobs if the cluster is heavily utilised or the paying lab is queuing up large jobs, though this will be much
reduced.

Pricing

GPUs:
$1.80 per GPU-hour used

For example, if a user runs an experiment with 8 GPUs over 48 hours
that is using the GPUs 60% of the time, this would cost $414

Storage:
$0.0004 per GB-hour of total storage for users that have this priority boost

Data egress:
$0.0085 per GB

The priority boost would mean that your jobs would be at the top of the queue (with the exception of CAIS jobs) but would need to wait for any existing jobs to finish running, if the cluster is at capacity. So the time saved would depend on how long the queue is at that point in time. The simplest approach would likely be to set up a partition for you that would have priority over the partition for free users, sharing the same underlying computing resources. You can think of it as being similar to pre-emption except that existing jobs would finish running before yours would start.

The fees charged would be primarily based on the number of GPU-hours consumed. We can be flexible on adding or removing people. The goal behind the minimum commitment is to ensure that the lab is committed to the paid option for a reasonable length of time rather than switching frequently between paid and free access.

Let me know if you have any other questions. If you're happy to go ahead with the approach discussed above, please indicate when you'd like to start. We can share an agreement for you to sign and get this set up with a lead time of around a week.

<<<

Thanks for following up. 20-25 is a relatively large number of users, so it would be helpful to get a better sense of how compute-intensive your research will be. This is to make sure we can balance your lab's needs with those of other users. Could you share details on any of the following data points to help us to understand your lab's needs:
How many GPUs (and what type) your team currently uses around peak times (e.g. around submission deadlines or when multiple projects are overlapping)
How many A100s you would ideally like to have access to in order to support all your labs' projects
Which current or upcoming projects you expect to be most compute-intensive (for example will you be training models or doing adversarial training runs?)

<<<

we can start sooner with a smaller group of users (like ~5)?  
I guess we'd want to have 1-5 GPUs per core user most of the time (many of the interns will likely not even need CAIS resources, but would like to give them access in case they can make use of it).
I'd also imagine users wanting to use dozens of GPUs at a time for some larger scale experiments, but probably a lot of that can happen on Cambridge HPC.

Also, I forget if we've discussed if it should be easy to get interactive instances on the CAIS cluster?

In my experience, it's been easy/fast to get interactive instances on the CAIS cluster.

<<<

We have a shared partition for all cluster users which is reserved for interactive work, which we monitor to ensure enough resources are available. If this doesn't work, we could discuss setting up a separate solution for your group.

To make sure that sufficient GPUs are available for other users around peak times, we'd like to have a cap on the number of GPUs included in the partition where your lab would have priority. We could potentially start by setting this at 64 GPUs and then re-visit this after the ICLR deadline in September. Unfortunately, we'd already done our latest planning around capacity and onboarded several new research labs at the start of June before we heard from you, which means that we are slightly constrained in terms of how much capacity we can easily carve out for your lab in the short term. Beyond September, we have more flexibility and will also have a more accurate sense of the cluster's utilisation (there is usually a lull over the summer holidays).

Let me know if this approach would work from your perspective and if this would be enough compute for your near term needs. Once we've found an approach that works for everyone, we can share a draft agreement for you to review.

<<<

We'd prefer to limit the number of users where possible. I expect the cluster to be very busy around the ICLR deadline, since the cluster always gets more congested close to deadlines and the number of labs using it has increased over the last few months. Having said this, if there are people that are working now and are confident they'll wrap up most of their experiments before September, adding more of these would be less of a concern.

please try to be cooperative in your use of the cluster, and communicate to each other and/or me early and often about any conflicts regarding resource use/allocation.  If we're running out of compute, I want to know, so I can help make project prioritization decisions.