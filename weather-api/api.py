import json
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

hostname = "localhost"
port = 8000

title = "TensorFlow-Weather-API"

foo = 18.2
bar = 0.02


class WeatherApi(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info("GET STARTED")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response_data = {
            "temperature": foo,
            "humidity": bar
        }

        response_json = json.dumps(response_data)
        self.wfile.write(bytes(response_json, "utf-8"))


if __name__ == '__main__':
    webServer = HTTPServer((hostname, port), WeatherApi)
    print("Server started http://%s:%s" % (hostname, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")