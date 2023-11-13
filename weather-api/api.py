import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

hostname = "localhost"
port = 8000

title = "TensorFlow-Weather-API"


class WeatherApi(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info("GET STARTED")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>{}</title></head>".format(title), "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == '__main__':
    webServer = HTTPServer((hostname, port), WeatherApi)
    print("Server started http://%s:%s" % (hostname, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
