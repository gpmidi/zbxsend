'''
Created on Jan 11, 2014

@author: Paulson McIntyre (GpMidi) <paul@gpmidi.net>
@author: Sergey Kirillov <https://github.com/pistolero>
@license: BSD 
@note: Originally part of https://github.com/pistolero/zbxsend/blob/master/zbxsend.py
'''
import time
import logging
try:
    import json  # @UnresolvedImport
except:
    import simplejson as json  # @UnresolvedImport @Reimport


class Metric(object):
    """ A Zabbix metric data point 
    """
    l = logging.getLogger(Metric.__module__ + "." + Metric.__class__.__name__)

    def __init__(self, host, key, value, clock = None):
        self.host = host
        self.key = key
        self.value = value
        self.clock = clock

    def __repr__(self):
        if self.clock is None:
            return 'Metric(%r, %r, %r)' % (self.host, self.key, self.value)
        return 'Metric(%r, %r, %r, %r)' % (self.host, self.key, self.value, self.clock)

    def toZbxJSON(self):
        """ Convert to JSON that Zabbix will accept """
        # Zabbix has very fragile JSON parser, and we cannot use json to dump whole packet
        clock = self.clock or time.time()
        ret = (
               '\t\t{\n'
               '\t\t\t"host":%s,\n'
               '\t\t\t"key":%s,\n'
               '\t\t\t"value":%s,\n'
               '\t\t\t"clock":%s}'
               ) % (
                    json.dumps(self.host),
                    json.dumps(self.key),
                    json.dumps(self.value),
                    clock,
                    )
        self.l.log(3, "Seralized %r to %r", self, ret)
        return ret
