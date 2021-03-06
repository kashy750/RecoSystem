#!/usr/bin/env python

class RecoError(Exception):
    
    """Base class for Recommendation errors"""

    @property
    def message(self):
        '''Returns the first argument used to construct this error.'''
        return self.args[0]