from http.server import HTTPServer
from .handler import DataHandler

class DataServer(HTTPServer):
    def __init__(self, queue, linked_list, host='localhost', port=8000):
        self._queue = queue()
        self._list = linked_list()
        super().__init__((host, port),
            lambda *args: DataHandler(self._queue, self._list, *args))

    def run(self):
        self.serve_forever()