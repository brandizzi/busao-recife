#!/usr/bin/env python
class UTF8EncodedStr(object):

    def __str__(self):
        return unicode(self).encode('utf-8')

class CodedAndNamed(object):

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __eq__(self, other):
        return (
            self is other or
            (self.code == other.code and self.name == other.name)
        )

    def __unicode__(self):
        return u"{className}({code}, {name})".format(
            className=self.__class__.__name__,
            code=repr(self.code),
            name=repr(self.name)
        )

class Route(CodedAndNamed, UTF8EncodedStr):

    def __init__(self, code, name, price=0.0, company=None, info=None):
        CodedAndNamed.__init__(self, code, name)
        self.price = price
        self.company = company
        self.info = info

    def __unicode__(self):
        return u"{className}({code}, {name}, {price}, {company})".format(
            className=self.__class__.__name__,
            code=repr(self.code),
            name=repr(self.name),
            price=repr(self.price),
            company=repr(self.company)
        )

class Itinerary(CodedAndNamed, UTF8EncodedStr):

    def __init__(self, code, name):
        CodedAndNamed.__init__(self, code, name)

class Trajectory(UTF8EncodedStr):

    def __init__(self, places):
        self.places = places

    def __unicode__(self):
        return (
            u"{className}("
            ", ".join(str(place) for place in self.places)
        )

class Place(UTF8EncodedStr):

    def __init__(self, municipality, location):
        self.municipality = municipality
        self.location = location

    def __unicode__(self):
        return u"{className}({municipality}, {location})".format(
            className=self.__class__.__name__,
            municipality=repr(self.municipality),
            location=repr(self.location)
        )
