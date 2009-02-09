// Basic example for passing PMI object (references) via PMI.
//
//
// Execute via:
//
//   > mpiexec -n 2 pass_obj

#include <iostream>
#include <pmi/pmi.hpp>
#include <logging/log4espp.hpp>
#include <mpi.h>

using namespace std;

// Simple class that "computes a message" (actually, it only returns
// the MPI thread, but the principle is sound, eh?)
class A 
  : public pmi::ParallelClass<A> 
{
public:
  unsigned short computeMessage() { 
    return pmi::getWorkerId();
  }
};

PMI_REGISTER_CLASS("A", A);

class B 
  : public pmi::ParallelClass<B> 
{

  A *a;

public:
  void setA(A& _a) {
    // invoke setAWorker in parallel
    invoke<&B::setAWorker>();

    // broadcast object "a"
    pmi::broadcastObject(_a);

    // set the local copy
    a = &_a;
  }

  void setAWorker() {
    // receive object "a"
    a = pmi::receiveObjectPtr<A>();
  }

  std::string getMessage() {
    // invoke the parallel method
    invoke<&B::getMessageWorker>();

    // compute the message
    unsigned short myMsg = _getMessage();

    // gather the messages from the different workers
    int size = MPI::COMM_WORLD.Get_size();
    unsigned short allMsg[size];
    MPI::COMM_WORLD.Gather(&myMsg, 1, MPI::UNSIGNED_SHORT,
			   allMsg, 1, MPI::UNSIGNED_SHORT, 0);
    // compose and print the message
    ostringstream ost;
    ost << "getMessage(): Got \"Hello World\" from workers: " << allMsg[0];
    for (int i = 1; i < size; i++)
      ost << ", " << allMsg[i];
    return ost.str();
  }

  void getMessageWorker() {
    // compute the message
    unsigned short myMsg = _getMessage();

    // send the message to the controller
    MPI::COMM_WORLD.Gather(&myMsg, 1, MPI::UNSIGNED_SHORT, 
			   0, 0, MPI::UNSIGNED_SHORT, 0);
  }

  short unsigned _getMessage() {
    return a->computeMessage();
  }
};

PMI_REGISTER_CLASS("B", B);
PMI_REGISTER_METHOD("setAWorker", B, setAWorker);
PMI_REGISTER_METHOD("getMessageWorker", B, getMessageWorker);

int main(int argc, char* argv[]) {
  // Required by MPI
  MPI::Init(argc, argv);
  // Required by the logging system
  LOG4ESPP_CONFIGURE();

  // mainLoop will return "false" only on the controller
  if (!pmi::mainLoop()) {
    A a;
    B b;
    
    b.setA(a);
    cout << b.getMessage() << endl;

    // Stop the workers
    pmi::endWorkers();
  } 


  MPI::Finalize();
  return 0;
}
