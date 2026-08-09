class UnableToWriteToFile(Exception):
    """Raised when a file cannot be written."""
    pass

class TrunkNotExists(Exception):
    '''Raised when a Trunk cannot be found by the system in the files'''
    pass

class BranchNotExixts(Exception):
    '''Raised whenn a Branch cannot be found by the system in the files'''
    pass

class BranchNameNotAccepted(Exception):
    '''Raised when the brach name cannot be accepted'''
    pass

class ValueNotFound(Exception):
    '''Raised when value for a key cannot be found'''
    pass

class KeyNotFound(Exception):
    '''Raised when key does not exist or cannot be found'''
    pass

class WrongPassword(Exception):
    def __init__(self, moreinfo: str):
        super().__init__(f"Wrong password.\n{moreinfo}")