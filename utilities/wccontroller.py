# wccontroller.py
# Version: 0.0.1.010
# Last Changes: 01/01/2025

from utilities.wcresponse import WoodchipperCoreResponse as WCResponse

class WoodchipperController:
    def __init__(self, handlers):
        self.request = None
        self.data = None
        self.handlers = handlers
        self.response = WCResponse()

    def process_request(self, process_request):
        self.request = process_request
        self.response.build_from_request(self.request)
        handler_id = self.request.mode
        if handler_id:
            self.response.mode = handler_id
            handler_type = self.handlers[handler_id]
            handler = handler_type(self.request, self.response)
            self.data = handler.run()
            self.response.data = self.data
            self.response.success = True
        else:
            self.response.error = "Unable to figure out which handler should operate on the request."