# Generalized Linear Model

[https://www.mygreatlearning.com/blog/generalized-linear-models/](https://www.mygreatlearning.com/blog/generalized-linear-models/)

GLM models allow us to build a linear relationship between the response and predictors, even though their underlying relationship is not linear. This is made possible by using a link function, which links the response variable to a linear model. 

Unlike Linear Regression models, the error distribution of the response variable need not be normally distributed. The errors in the response variable are assumed to follow an exponential family of distribution (i.e. normal, binomial, Poisson, or gamma distributions). Since we are trying to generalize a linear regression model that can also be applied in these cases, the name Generalized Linear Models.

[https://online.stat.psu.edu/stat504/lesson/6/6.1](https://online.stat.psu.edu/stat504/lesson/6/6.1)

- What are the steps to using a Generalized Linear Model?
    1. Choose the appropriate distribution for the response (to predict; continuous) variable: The choice of distribution depends on the nature of the response variable. For example, if the response variable is binary (e.g., success or failure), you can use the Bernoulli distribution. If the response variable is a count (e.g., number of accidents), you can use the Poisson distribution. If the response variable is continuous and has a normal distribution, you can use the linear regression model.
    2. Identify the explanatory variables: The explanatory variables are the variables that you use to explain or predict the response variable. They can be continuous or categorical.
    3. Model specification: Specify the form of the relationship between the response variable and the explanatory variables. This involves choosing a link function that relates the expected value of the response variable to the linear predictor of the explanatory variables.
    4. Model estimation: Estimate the parameters of the GLM using maximum likelihood estimation. This involves finding the values of the parameters that maximize the likelihood of the observed data.
    5. Model evaluation: Evaluate the goodness-of-fit of the GLM using various statistical measures, such as deviance, residual plots, and information criteria.
    6. Model interpretation: Interpret the estimated parameters of the GLM in the context of the research question. This involves understanding the direction and strength of the relationship between the response variable and the explanatory variables.
    7. Predictive modeling: Use the GLM to make predictions on new data. This involves plugging in the values of the explanatory variables into the GLM equation to obtain the predicted value of the response variable.
    
- In Python
    
    Let's say 'y' follows a Poisson distribution and the explanatory variables are 'x1', 'x2', and 'x3'. Use a log link function.
    
    ```
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    
    # Create a GLM formula
    formula = 'y ~ x1 + x2 + x3'
    
    # Specify the distribution and link function
    glm = smf.glm(formula=formula, data=data, family=sm.families.Poisson(sm.families.links.log()))
    
    # Fit the GLM using maximum likelihood estimation
    model = glm.fit()
    ```
    
    Evaluate the goodness-of-fit of the GLM using various statistical measures.
    
    ```
    # Print the summary of the GLM
    print(model.summary())
    
    # Plot the residuals
    sm.graphics.plot_residuals(model, "pearson", fig=plt.figure(figsize=(10, 8)))
    ```
    
    Model interpretation: Interpret the estimated parameters of the GLM in the context of the research question.
    
    ```
    # Print the estimated parameters
    print(model.params)
    ```
    
    Predictive modeling: Use the GLM to make predictions on new data.
    
    ```
    # Create a new dataset for prediction
    new_data = pd.DataFrame({'x1': [1, 2, 3], 'x2': [4, 5, 6], 'x3': [7, 8, 9]})
    
    # Make predictions on new data
    predictions = model.predict(new_data)
    ```