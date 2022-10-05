import numpy as np 

def get_deviation(data):
    """
    yo
    """
    return data - np.mean(data)

def get_regression_slope_intercept(x_axis, y_axis):
    """
    Ordinary Least Squares Linear Regression.
    Returns slope and intercept. For only one independent variable.
    
    Slope: covariance divided by variance of independent* variable
    Intercept: mean of dependent variable** divided by slope times mean of independent variable
    *Independent variable = x_axis, what we use to predict
    **Dependent variable = y_axis, what we want to predict based on x_axis
    
    """
    dev_x = get_deviation(x_axis)
    dev_y = get_deviation(y_axis)
    
    slope = np.sum(dev_x*dev_y)/np.sum(dev_x*dev_x)
    intercept = np.mean(y_axis) - slope*np.mean(x_axis)
    return slope, intercept

def get_linear_regression_two_independent_variables(x1_axis, x2_axis, y_axis):
    """
    geting crazy here!
    Wonder if it's possible to extrapolate a formula for infinite axes...
    Got it from http://faculty.cas.usf.edu/mbrannick/regression/Part3/Reg2.html
    """
    dev_x1 = get_deviation(x1_axis)
    dev_x2 = get_deviation(x2_axis)
    dev_y = get_deviation(y_axis)
    
    coef_1 =  (
        ((np.sum(dev_x2*dev_x2)*np.sum(dev_x1 * dev_y)) - (np.sum(dev_x1 * dev_x2)*np.sum(dev_x2*dev_y)))
        /
        (np.sum(dev_x1**2)*np.sum(dev_x2**2) - np.sum(dev_x1 * dev_x2)**2)
    )
    
    coef_2 =  (
        ((np.sum(dev_x1*dev_x1)*np.sum(dev_x2 * dev_y)) - (np.sum(dev_x1 * dev_x2)*np.sum(dev_x1*dev_y)))
        /
        (np.sum(dev_x1**2)*np.sum(dev_x2**2) - np.sum(dev_x1 * dev_x2)**2)
    )
    intercept = np.mean(y_axis) - coef_1*np.mean(x1_axis) - coef_2*np.mean(x2_axis)
    return coef_1, coef_2, intercept
    
