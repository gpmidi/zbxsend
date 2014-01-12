'''
Created on Jan 12, 2014

@author: Paulson McIntyre (GpMidi) <paul@gpmidi.net>
'''

# Built-in
import logging
import time
import datetime
import threading
import random
import sys

# Others

# Ours
from mon.zbx.comm.metric import Metric
from mon.zbx.comm.zbxServer import ZabbixServer


logging.basicConfig(
                    # level = logging.DEBUG,
                    level = 1,
                    )


def sendSimple(server,host='localhost',key='test',count=500):
    log = logging.getLogger('mon.zbx.comm._test.sendSimple')
    startTime=datetime.datetime.now()
    for i in xrange(0,count):
        metric = Metric(host = host, key = key, value = float(i * time.time() * 0.000001))
        server.queueMetric(metric=metric,priority=10)
        time.sleep(random.randint(0, 20) * 0.01)
    endTime=datetime.datetime.now()
    log.info("Done sending %d records in %r",count,endTime-startTime)
    

if __name__ == '__main__':
    log = logging.getLogger('mon.zbx.comm._test.__main__')
    try:
        import mon.zbx.comm._testSettings as settings
    except ImportError, e:
        log.exception("Failed to load settings: %r", e)
        sys.exit(1)
    server = ZabbixServer(
                        host = settings.ZABBIX_HOST,
                        port = settings.ZABBIX_PORT,
                        )
    server.start()

    sendSimple(server, host = settings.HOST, key = settings.KEY, count = 500)

    server.stopRunning()

