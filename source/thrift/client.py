#!/usr/bin/env python

import sys
sys.path.append('gen-py')

from alerta import *
from alerta.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

try:
    # transport = TSocket.TSocket('localhost', 9090)
    # transport = TTransport.TBufferedTransport(transport)
    transport = TTransport.TMemoryBuffer()
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    alert = Alert()
    alert.resource = 'foo'
    alert.event = 'bar'

    print alert

    alert.write(protocol)
    bytes = transport.getvalue()

    print repr(bytes)

    thrift_in = TTransport.TMemoryBuffer(bytes)
    protocol_in = TBinaryProtocol.TBinaryProtocol(thrift_in)
    receivedAlert = Alert()
    receivedAlert.read(protocol_in)
    print receivedAlert

except Thrift.TException as tx:
    print '%s' % tx.message