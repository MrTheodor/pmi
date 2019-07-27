import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pmi import pmi
from setup_tests import pmi_name, mockFunc, add

mockFuncCalled = None

# On the frontend
if __name__ != pmi_name:
    # load the module on all workers
    pmi.execfile_(__file__)

# Mock function, visible only to the workers
if __name__ != pmi_name:
    # test pmi calls
    class TestCall(unittest.TestCase):
        def tearDown(self):
            pmi.sync()

        def testBuiltinFunction(self):
            self.assertEqual(list(pmi.call(zip)), [])
            # by string
            self.assertEqual(list(pmi.call('zip')), [])

        def testFunction(self):
            self.assertEqual(pmi.call(mockFunc), 42)
            self.assertFalse('mockFunc2' in globals())

        def testBadArgument(self) :
            if pmi.isController:
                self.assertRaises(TypeError, pmi.call, 1)
                self.assertRaises(ValueError, pmi.call, lambda x: x)
                self.assertRaises(NameError, pmi.call, 'doesntexist')

if __name__ == '__main__':
    unittest.main()
