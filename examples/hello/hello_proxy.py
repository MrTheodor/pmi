##################################################
## Serial code
##################################################
import pmi

pmi.setup()
pmi.execfile_('hello_class.py')

# create a frontend class via the proxy
class Hello(object, metaclass=pmi.Proxy):
    pmiproxydefs = {
        'cls': 'HelloLocal',
        'pmiinvoke': ['__call__'],
        'pmiproperty': ['name']
    }

# use the class
hello = Hello('Olaf')
print(('\n'.join(hello())))
