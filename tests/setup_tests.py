import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

pmi_name = 'pmi.pmi'

# Mock functions, visible to worker and frontend
def mockFunc(arg=None, *args, **kwds):
    global mockFuncCalled, mockFuncArg, mockFuncArgs, mockFuncKwds
    mockFuncCalled = True
    mockFuncArg = arg
    mockFuncArgs = args
    mockFuncKwds = kwds
    return 42

def add(a, b):
    return a + b

# Mock function, visible only to the workers
if __name__ == pmi_name:
    def mockFunc1(arg=None, *args, **kwds):
        global mockFunc1Called, mockFunc2Arg, mockFunc2Args, mockFunc2Kwds
        mockFunc1Called = True
        mockFunc1Arg = arg
        mockFunc1Args = args
        mockFunc1Kwds = kwds
        return 51
