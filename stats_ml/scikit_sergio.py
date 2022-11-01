import numpy as np
import pandas as pd 


def get_mean(data):
    """
    Mean: sum / len data
    equivalent to np.mean()

    """
    return sum(data)/len(data)

def get_deviation(data):
    """
    Returns array: data minus mean(data)
    I don't know of any equivalent
    """
    return data - get_mean(data)

def get_mean_sum_square_deviation(data, is_sample = False):
    """
    Returns mean of sum of deviation squared.
    Similar to np.var()
    """
    n = len(data) - 0
    if is_sample == True:
        n = n-1
    return sum(get_deviation(data)**2)/n

def get_root_mean_sum_square_deviation(data, is_sample = False):
    """
    Returns root of mean sum square of deviation
    Similar to np.std()
    """
    return np.sqrt(get_mean_sum_square_deviation(data, is_sample = is_sample))

def get_variance(data, is_sample = False):
    """
    Return variance. Is just a mask for get_mean_sum_square_deviation().
    Similar to np.var()
    """    
    return get_mean_sum_square_deviation(data, is_sample)

def get_std(data, is_sample = False):
    """
    Returns standar deviation. Is just a mask for get_root_mean_sum_square_deviation()
    """
    return get_root_mean_sum_square_deviation(data, is_sample)
    
def get_cov(data1, data2, is_sample = False):
    """
    Returns covariance of data1 and data2.
    Returns mean of deviation of data1 multiplied by deviation of data2.
    See get_deviation()

    Similar to np.cov()

    """
    n = len(data1)
    if is_sample == True:
        n = n-1
    return sum(get_deviation(data1) * get_deviation(data2))/n
    
def get_pearson_corr(data1, data2):
    """
    Returns pearson coefficient correlation.
    Returns covariance divided by product of standard deviation of data1 and data2
    """
    return get_cov(data1, data2)/(get_std(data1) * get_std(data2))

def get_regression_slope_intercept(x_axis, y_axis):
    """
    Ordinary Least Squares Linear Regression.
    Returns slope and intercept. For only one independent variable.
    Equivalent of:
    - statsmodels.formula.api.ols('dep_col~indep_col', data = df).fit().params
    - np.polyfit(x,y, deg = 1) # for only one independent variable
    - sklearn.linear_model.LinearRegression().fit(X = df[['indep_col']], y = df['dep_col]).coef_,
    sklearn.linear_model.LinearRegression().fit(X = df[['indep_col']], y = df['dep_col]).intercept_ 


    
    Slope/coef/name of dependent column: covariance divided by variance of independent* variable
    Intercept: mean of dependent variable** divided by slope times mean of independent variable

    

    *Independent variable = x_axis, what we use to predict
    **Dependent variable = y_axis, what we want to predict based on x_axis
    
    """
    dev_x = get_deviation(x_axis)
    dev_y = get_deviation(y_axis)
    
    slope = np.sum(dev_x*dev_y)/np.sum(dev_x*dev_x)
    intercept = get_mean(y_axis) - slope*get_mean(x_axis)
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
    intercept = get_mean(y_axis) - coef_1*get_mean(x1_axis) - coef_2*get_mean(x2_axis)
    return coef_1, coef_2, intercept
    
    


def get_regression_ymodel(x_axis, y_axis):
    """
    Obtains optimal line of least squares.
    Calculates slope and intercept from arrays x_axis and y_axis and
    applies results to x_axis.

    Utilizes get_regression_slope_intercept()

    Equivalent of:
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
    return get_mean_sum_square_deviation(residual)

def get_ymodel_rmse(x_axis, y_axis):
    """
    Root Mean Squared Error, or RMSE.
    Formula: root mean of squares.
    Data: residuals - y_data minus y_model (dependent variable minus predicted values)
    
    Same formula as used for standard deviation, but for residuals.
    
    Unit: [y_data unit]. For ex: USD
    
    """
    residual = get_residual(x_axis, y_axis)
    return get_root_mean_sum_square_deviation(residual)

def get_r2(x_axis, y_axis):
    """
    yo
    """
    var = get_variance(y_axis)    
    mse = get_ymodel_mean_squared_error(x_axis, y_axis)
    return 1-(mse/var)





