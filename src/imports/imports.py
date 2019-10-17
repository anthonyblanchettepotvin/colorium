import sys


def dropCachedImports(*packagesToUnload):
    """
    Drops all the modules specified in the list.
    """ 
    
    
    def shouldUnload(module):
        for packageToUnload in packagesToUnload:
            if module.startswith(packageToUnload):
                return True
        return False
        
    
    for i in sys.modules.keys()[:]:
        if shouldUnload(i):
            print "Dropping module", i
            del sys.modules[i]
