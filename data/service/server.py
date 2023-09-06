#!/usr/bin/python3 env

import http.server
import socketserver
import json
import os

# Get the directory of the Python script (current script)
script_directory = os.path.dirname(os.path.abspath('/.unknown/service/'))

os.chdir(script_directory)

class MagicAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/users':
            api_key = self.headers.get('Authorization', '').replace('Bearer ', '')
            if api_key == '5Rj7D9sQxZ2cCpGnWvAeF6hT4yXwU8zK':
                response_data = {
                    "ssh_user1": "cyberrav",
                    "password1": "g0t_my_a1ms",
                    
                    "ssh_user2": "justin",
                    "password2": "find_a_new_one!!",
                }
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode())
            else:
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b'Unauthorized')
        
        # Serve the robots.txt when the robots.txt ("/robots.txt") is requested
        elif self.path == '/robots.txt':
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                with open('/.unknown/service/robots.txt', 'rb') as html_file:
                    self.wfile.write(html_file.read())
                    
        else:
            # Serve the HTML file when the root path ("/") is requested
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                with open('/.unknown/service/index.html', 'rb') as html_file:
                    self.wfile.write(html_file.read())
                    
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'Not Found')


if __name__ == '__main__':
    PORT = 7888
    httpd = socketserver.TCPServer(("", PORT), MagicAPIHandler)
    print("Serving at port {}".format(PORT))
    httpd.serve_forever()

