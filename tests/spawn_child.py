from mpi4py import MPI
import numpy

world = MPI.COMM_WORLD

print('Child world task %d: Started.' % world.rank)
intercomm = world.Get_parent()

buf = numpy.empty(100, dtype='f')
intercomm.Bcast([buf, MPI.LONG])
print('Child task %d, got broadcast message %s via intercomm.'
      % (intercomm.rank, buf))

intercomm.Disconnect()

# print('Child task %d: Merging.' % intercomm.rank)
# newcomm = intercomm.Merge(True)

# while True:
#     msg = newcomm.bcast()
#     print('Task %d, got %s' % (newcomm.rank, msg))
