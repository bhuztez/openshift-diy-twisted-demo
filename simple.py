from twisted.web import resource

class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html><head><title>Twisted on OpenShift</title></head><body>It works!</body></html>"

