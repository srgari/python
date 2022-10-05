import numpy as np
import pandas as pd 


def get_mean(data):
    """
    yo
    """
    return np.mean(data)

def get_deviation(data):
    """
    yo
    """
    return data - get_mean(data)

def get_mean_sum_square(data, is_sample = False):
    """
    yo
    """
    n = len(data) - 0
    if is_sample == True:
        n = n-1
    return sum(get_deviation(data)**2)/n

def get_root_mean_sum_square(data, is_sample = False):
    """
    yo
    """
    return np.sqrt(get_mean_sum_square(data, is_sample = is_sample))

def get_variance(data, is_sample = False):
    """
    yo
    """    
    return get_mean_sum_square(data, is_sample)

def get_std(data, is_sample = False):
    """
    yo
    """
    return get_root_mean_sum_square(data, is_sample)
    
def get_cov(data1, data2, is_sample = False):
    """
    yo
    """
    n = len(data1)
    if is_sample == True:
        n = n-1
    return sum(get_deviation(data1) * get_deviation(data2))/n
    
def get_pearson_corr(data1, data2):
    """
    yo
    """
    return get_cov(data1, data2)/(get_std(data1) * get_std(data2))

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
    intercept = get_mean(y_axis) - slope*get_mean(x_axis)
    return slope, intercept
    
def get_regression_ymodel(x_axis, y_axis):
    """
    yo
    """
    slope, intercept = get_regression_slope_intercept(x_axis, y_axis)
    y_model = x_axis * slope + intercept
    return y_model
    
def get_residual(x_axis, y_axis):
    """
    yo
    """
    y_model = get_regression_ymodel(x_axis, y_axis)
    return y_axis - y_model
    
def get_ymodel_mse(x_axis, y_axis):
    """
    Mean Squared Error, or MSE.
    Formula: mean sum of squares.
    Data: residuals - y_data minus y_model (dependent variable minus predicted values)
          
    Same formula as used for variance, but applied on the residuals.
    
    Unit: [y_data unit] squared. For ex: if in dollars, unit is USD²
    """
    residual = get_residual(x_axis, y_axis)
    return get_mean_sum_square(residual)

def get_ymodel_rmse(x_axis, y_axis):
    """
    Root Mean Squared Error, or RMSE.
    Formula: root mean of squares.
    Data: residuals - y_data minus y_model (dependent variable minus predicted values)
    
    Same formula as used for standard deviation, but for residuals.
    
    Unit: [y_data unit]. For ex: USD
    
    """
    residual = get_residual(x_axis, y_axis)
    return get_root_mean_sum_square(residual)

def get_r2(x_axis, y_axis):
    """
    yo
    """
    var = get_variance(y_axis)    
    mse = get_ymodel_mean_squared_error(x_axis, y_axis)
    return 1-(mse/var)

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
    intercept = get_mean(y_axis) - coef_1*get_mean(x1_axis) - coef_2*get_mean(x2_axis)
    return coef_1, coef_2, intercept
    
    




