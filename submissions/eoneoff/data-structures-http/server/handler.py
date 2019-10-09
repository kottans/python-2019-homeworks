from http.server import BaseHTTPRequestHandler
import json
import cgi

class DataHandler(BaseHTTPRequestHandler):
    def __init__(self, stack, linked_list, *args):
        self._stack = stack
        self._list = linked_list
        super().__init__(*args)

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    @staticmethod
    def _value_is_valid(value):
        return type(value) == str \
            or type(value) == int \
            or type(value) == float

    def _request_is_json(self):
        ctype,_ = cgi.parse_header(self.headers.get('content-type'))
        if ctype!='application/json':
            self.send_error(400, 'Wrong content type')
            return False
        else: return True

    def _get_request_data(self):
        length = int(self.headers.get('content-length'))
        return json.loads(self.rfile.read(length))

    def _get_structure_type(self):
        structure_type = self.path.split('/')[1]
        return structure_type if structure_type  in ['stack', 'list'] else None
        

    def do_GET(self):
        if(self._get_structure_type() == 'list'):
            self._set_headers()
            self.wfile.write(str.encode(json.dumps({'data':self._list.show_list()})))

    def do_POST(self):
        if(self._request_is_json()):
            data = self._get_request_data()
            if DataHandler._value_is_valid(data['data']):
                structure_type = self._get_structure_type()
                if structure_type == 'stack':
                    self._stack.push(data['data'])
                    self.send_response(200)
                    self.end_headers()
                elif structure_type == 'list':
                    successor = data.setdefault('successor')
                    if not successor or DataHandler._value_is_valid(successor):
                        try:
                            self._list.insert(data['data'], successor)
                            self.send_response(200)
                            self.end_headers()
                        except ValueError as err:
                            self.send_error(400, str(err))
                    else: self.send_error(400, 'Wrong successor format')
            else: self.send_error(400, 'Wrong value type')
        else: self.send_error(400, 'Wrong content type')

    def do_DELETE(self):
        structure_type = self._get_structure_type()
        if structure_type == 'stack':
            self._set_headers()
            self.wfile.write(str.encode(json.dumps({'data': self._stack.pop()})))
        elif structure_type == 'list':
            if self._request_is_json():
                data = self._get_request_data()
                if DataHandler._value_is_valid(data['data']):
                    try:
                        self._list.remove(data['data'])
                        self.send_response(200)
                        self.end_headers()
                    except ValueError as err:
                        self.send_error(400, str(err))
                else: self.send_error(400, 'Wrong data type')
            else:  self.send_error(400, 'Wrong content type')
