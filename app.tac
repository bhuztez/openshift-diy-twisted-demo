import os

from twisted.application import internet, service
from twisted.web import server, static

from autobahn import websocket
from autobahn.resource import WebSocketResource, HTTPChannelHixie76Aware


class EchoProtocol(websocket.WebSocketServerProtocol):
   def onMessage(self, msg, binary):
      self.sendMessage(msg, binary)


domain = os.environ['OPENSHIFT_APP_DNS']
port = int(os.environ['OPENSHIFT_INTERNAL_PORT'])
interface = os.environ['OPENSHIFT_INTERNAL_IP']

factory = websocket.WebSocketServerFactory("ws://%s:%d"%(domain,port))
factory.protocol = EchoProtocol
factory.setProtocolOptions(allowHixie76 = True)

resource = WebSocketResource(factory)

root = static.File(".")
root.putChild("ws", resource)

site = server.Site(root)
site.protocol = HTTPChannelHixie76Aware
web_service = internet.TCPServer(port, site, interface=interface)

application = service.Application("OpenShift Twisted DIY demo")
web_service.setServiceParent(application)
