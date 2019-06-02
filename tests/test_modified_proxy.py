import unittest
from pickle import PicklingError

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pmi import pmi

from mock_proxy import MockProxyLocal, MockProxyLocalBase, MockProxyLocalDerived

pmi_name = 'pmi.pmi'


# On the frontend
if __name__ != pmi_name:
    # load the module on all workers
    pmi.execfile_(__file__)

    class TestModifiedProxy(unittest.TestCase):
        def testUserSuppliedInit(self):
            if pmi.isController:
                class MockProxy(metaclass=pmi.Proxy):
                    pmiproxydefs = dict(cls='MockProxyLocal')

                    def __init__(self, arg):
                        print('MockProxy.__init__')
                        self.arg = arg
                        self.pmiinit(arg+10)

                obj = MockProxy(42)
                pmiobj = obj.pmiobject
                self.assertTrue(hasattr(obj, 'arg'))
                self.assertEqual(obj.arg, 42)
                self.assertTrue(isinstance(pmiobj, pmi.MockProxyLocal))
                self.assertEqual(pmiobj.arg, 52)
                del(pmiobj)
                del(obj)
                pmi.sync()
            else:
                pmiobj = pmi.create()
                self.assertTrue(isinstance(pmiobj, pmi.MockProxyLocal))
                self.assertEqual(pmiobj.arg, 52)
                del(pmiobj)
                pmi.sync()

        def testUserSuppliedFunction(self):
            if pmi.isController:
                class MockProxy(object, metaclass=pmi.Proxy):
                    pmiproxydefs = dict(cls='MockProxyLocal')

                    def f4(self):
                        self.pmiobject.called = "f4"
                        return 72

                obj = MockProxy()
                pmiobj = obj.pmiobject
                self.assertEqual(obj.f4(), 72)
                pmi.sync()
                self.assertEqual(pmiobj.called, 'f4')
                del(obj)
                pmi.sync()
            else:
                pmiobj = pmi.create()
                pmi.sync()
                self.assertFalse(hasattr(pmiobj, 'called'))
                pmi.sync()


if __name__ == '__main__':
    unittest.main()

