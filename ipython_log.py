# IPython log file

import numpy as np
data = [i : np.r.rand() for i in range(7)]
data = {i : np.r.rand() for i in range(7)}
data = {i : np.random.rand() for i in range(7)}
data
an_apple = 27
an_example = 42
b =[1,2,3]
import datetime
get_ipython().magic('pinfo b')
def add_numbers(a,b):
    """
    Add two numbers together
    
    Returns
    -------
    the_sum: type of arguments
    """
    return a+ b
get_ipython().magic('pinfo add_numbers')
get_ipython().magic('pinfo2 add_numbers')
get_ipython().magic('psearch np.*load*')
get_ipython().magic('run ipython_script_test.py')
get_ipython().set_next_input('a = np.random.rand');get_ipython().magic('pinfo np.random.rand')
a = np.random.rand(100,100)
get_ipython().magic('timeit np.dot(a,a)')
a
a.value_counts
a.[a]value_counts
get_ipython().magic('pinfo value_counts')
get_ipython().magic('pinfo %reset')
plot(randn(1000).cumsum)
showplot()
plot.(randn(1000).cumsum)
show.plot()
get_ipython().magic('pinfo plot')
2 ** 27
_
foo = 'bar'
foo
_30
_i30
exec _i30
exec '_i30'
get_ipython().magic('pinfo exec')
exec(_i30)
exec(_i30)
get_ipython().magic('logstart')
get_ipython().magic('logstop')
