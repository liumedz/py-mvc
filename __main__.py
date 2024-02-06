from http.server import HTTPServer
from controllers.controller_registry import ControllerRegistry
from controllers.weather_controller import WeatherController


ControllerRegistry.register(ControllerRegistry, "/", WeatherController())

# Set the port
port = 8000
# Create an HTTP server instance
httpd = HTTPServer(('localhost', port), ControllerRegistry)

print(f"Server started on localhost:{port}")
httpd.serve_forever()
