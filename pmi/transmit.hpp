#ifndef _PMI_TRANSMIT_HPP
#define _PMI_TRANSMIT_HPP

#include "pmi/types.hpp"
#include "pmi/basic_func.hpp"

using namespace std;

namespace pmi {
  // get the workerId of the executing process
  // corresponds to the MPI rank
  // 0 is the controller
  WorkerIdType getWorkerId();
    

  namespace transmit {
    //////////////////////////////////////////////////
    // Status definition
    //////////////////////////////////////////////////
    const unsigned short STATUS_OK = 0;
    const unsigned short STATUS_USER_ERROR = 1;
    const unsigned short STATUS_INTERNAL_ERROR = 2;
    const unsigned short STATUS_OTHER_ERROR = 3;
    

#ifdef CONTROLLER
    void endWorkers();

    void associateClass(const string &name, const IdType id);
    void associateMethod(const string &name, const IdType id);
    
    void create(const IdType classId,
		const IdType objectId);
    void invoke(const IdType classId, 
		const IdType methodId, 
		const IdType objectId);
    void destroy(const IdType classId,
		 const IdType objectId);
    void broadcastObject(const IdType classId,
			 const IdType objectId);

#ifndef PMI_OPTIMIZE
    // collect the results of the last operation from all workers
    // check for failure
    void gatherStatus();
#endif
#endif

#ifdef WORKER
    void reportOk();
    void reportError(unsigned char status, const string &what);

    // receive the next command from the controller and execute it
    // returns false if the stop worker command was received, true otherwise
    bool handleNext();
#endif
  }
}

#endif
