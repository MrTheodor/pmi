import pickle
import unittest

from setup_tests import pmi_name, mockFunc
from pmi import pmi



# Mock function, visible only to the workers
if __name__ != pmi_name:
    # load the module on all workers
    pmi.execfile_(__file__)
    # test passing arguments to a pmi call
    class TestPassArguments(unittest.TestCase):
        def setUp(self):
            global mockFuncArg, mockFuncArgs, mockFuncKwds
            mockFuncArg = None
            mockFuncArgs = None
            mockFuncKwds = None

        def tearDown(self):
            pmi.sync()

        def testSimple(self):
            global mockFuncArg
            pmi.call(mockFunc, 42)
            self.assertEqual(mockFuncArg, 42)
            self.assertEqual(mockFuncArgs, ())
            self.assertEqual(mockFuncKwds, {})

        def testList(self):
            global mockFuncArg, mockFuncArgs
            pmi.call(mockFunc, 42, 52, 62)
            self.assertEqual(mockFuncArg, 42)
            self.assertEqual(mockFuncArgs, (52, 62))
            self.assertEqual(mockFuncKwds, {})

        def testKeywords(self) :
            global mockFuncArg, mockFuncArgs, mockFuncKwds
            pmi.call(mockFunc, arg1=42, arg2=52)
            self.assertEqual(mockFuncArg, None)
            self.assertEqual(mockFuncArgs, ())
            self.assertEqual(mockFuncKwds, {'arg1' : 42, 'arg2' : 52})

        def testMixed(self) :
            global mockFuncArg, mockFuncArgs, mockFuncKwds
            pmi.call(mockFunc, 42, 52, 62, arg1=72, arg2=82)
            self.assertEqual(mockFuncArg, 42)
            self.assertEqual(mockFuncArgs, (52, 62))
            self.assertEqual(mockFuncKwds, {'arg1' : 72, 'arg2' : 82})

        def testController(self):
            global mockFuncArg, mockFuncArgs, mockFuncKwds
            obj = pmi.call(mockFunc, arg=42, __pmictr_arg=52)
            if pmi.isController:
                self.assertEqual(mockFuncArg, 52)
            else:
                self.assertEqual(mockFuncArg, 42)

        def testNonPicklable(self):
            if pmi.isController:
                self.assertRaises((AttributeError, pickle.PicklingError), pmi.call, mockFunc, arg=lambda x: x)

if __name__ == '__main__':
    unittest.main()
