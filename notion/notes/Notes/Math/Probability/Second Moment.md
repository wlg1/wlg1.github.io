# Second Moment

The second moment is related to the variance of a distribution, but it is not the same as the variance.

In probability theory and statistics, the variance of a distribution measures how much the values in the distribution vary from the mean of the distribution. It is defined as the average of the squared differences between the values in the distribution and the mean.

The second moment of a distribution is a related quantity that measures the average of the squared values in the distribution. It is defined as the integral of x^2 times the probability density function of the distribution, where x is the random variable and the integral is taken over the entire range of x.

The second moment of the gradients with respect to the input is used to estimate the curvature of the loss surface around the current input. This curvature can be thought of as a measure of the variation of the gradients with respect to the input. A high curvature indicates that the gradients vary a lot with respect to the input, while a low curvature indicates that the gradients are more stable and vary less with respect to the input.

---

So second moment is not variance, but variance of gradients?

Yes, that's correct. The second moment of the gradients with respect to the input is related to the variance of the gradients, not the variance of the inputs.

The gradients with respect to the input measure how the output of the neural network changes when the input is changed. The second moment of the gradients with respect to the input is a measure of the average of the squared gradients with respect to the input, which can be thought of as a measure of the variance of the gradients.