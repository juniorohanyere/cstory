"""Create a new element.
"""


class Create:
    def __init__(self, dname, fname, lname):
        """Initialize self. See help(type(self)) for accurate signature.
        """

        self._dname = dname
        self._fname = fname
        self._lname = lname

    def post(self, tag=None, msg):
        """Post a message to the screen.
        """
