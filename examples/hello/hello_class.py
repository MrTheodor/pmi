from mpi4py import MPI
import time
import os

# size = MPI.COMM_WORLD.Get_size()
# rank = MPI.COMM_WORLD.Get_rank()
# import pydevd_pycharm
#
# port_mapping = [45909, 42513]
# pydevd_pycharm.settrace('localhost', port=port_mapping[rank], stdoutToServer=True, stderrToServer=True)

print(os.getpid())

if __name__ != 'pmi.pmi':
    ##################################################
    ## Serial code
    ##################################################
    import pmi

    pmi.setup()
    pmi.execfile_(__file__)


    # create a frontend class
    class Hello(object):
        def __init__(self, name):
            self.pmiobj = pmi.create('HelloLocal', name)

        def __call__(self):
            return pmi.invoke(self.pmiobj, '__call__')


    # use the class
    hello = Hello('Olaf')
    print('\n'.join(hello()))
else:
    ##################################################
    ## Parallel code
    ##################################################

    class HelloLocal(object):
        def __init__(self, name):
            self.name = name

        def __call__(self):
            return 'Hello %s, this is MPI task %d!' % (self.name, MPI.COMM_WORLD.rank)
