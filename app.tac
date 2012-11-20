import os

from twisted.application import internet, service
from twisted.web import server

import simple

port = int(os.environ['OPENSHIFT_INTERNAL_PORT'])
interface = os.environ['OPENSHIFT_INTERNAL_IP']

site = server.Site(simple.Simple())
web_service = internet.TCPServer(port, site, interface=interface)

application = service.Application("OpenShift Twisted DIY demo")
web_service.setServiceParent(application)
