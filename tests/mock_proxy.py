
class MockProxyLocal:
    delCalled = False
    def __init__(self, arg=None, *args, **kwds):
        self.x = 17
        self.arg = arg
        self.args = args
        self.kwds = kwds
        MockProxyLocal.delCalled = False
    def __del__(self):
        if hasattr(MockProxyLocal, 'delCalled'):
            MockProxyLocal.delCalled = True
    def f(self):
        self.called = "f"
        return 42
    def f2(self):
        self.called = "f2"
        return 52
    def f3(self):
        self.called = "f3"
        return 62
    def f4(self):
        self.called = "f4"
        return 72

    def setX(self, v):
        self._x = v
    def getX(self):
        return self._x
    x = property(getX, setX)

class MockProxyLocalBase:
    def f(self, arg=None):
        self.arg = arg
        self.fCalled = True

    def g(self, arg=None):
        self.gArg = arg

class MockProxyLocalDerived(MockProxyLocalBase):
    def f(self, arg2=None, arg=42):
        self.arg2 = arg2
        self.fDerivedCalled = True
        MockProxyLocalBase.f(self, arg)

