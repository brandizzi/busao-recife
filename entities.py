#!/usr/bin/env python

class Itinerary(object):

    def __init__(self, code, name):
        self.code = code
        self.name = name
        
    def __unicode__(self):
        return u"Itinerary({code}, {name})".format(
            code=repr(self.code),
            name=repr(self.name))
    
    def __str__(self):
        return unicode(self).encode('utf-8')
