from mpi4py import MPI
import sys, numpy
import os

world = MPI.COMM_WORLD
print('Starter: Spawning.')
intercomm = world.Spawn(command = sys.executable,
                        args = [os.path.join(os.path.dirname(__file__), 'spawn_child.py')], maxprocs=1)

buf = numpy.empty(100, dtype='f')
print('Starter: Broadcasting %s to children via Intercomm.'
      % buf)
intercomm.Bcast([buf, MPI.LONG], root=MPI.ROOT)

print('End')

intercomm.Disconnect()
