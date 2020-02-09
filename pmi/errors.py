##################################################
## CONSTANTS AND EXCEPTIONS
##################################################

class InternalError(Exception):
    """Raised when PMI has encountered an internal error.

    Hopefully, this exceptions is never raised."""

    def __init__(self, msg, workerStr):
        self.msg = msg
        self.workerStr = workerStr

    def __str__(self):
        return self.workerStr + ': ' + self.msg

    def __repr__(self):
        return str(self)


class UserError(Exception):
    """Raised when PMI has encountered a user error.
    """

    def __init__(self, msg, workerStr):
        self.msg = msg
        self.workerStr = workerStr

    def __str__(self):
        return self.workerStr + ': ' + self.msg

    def __repr__(self):
        return str(self)
