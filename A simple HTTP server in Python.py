from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # Código de status HTTP 200 (OK)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from the server!")  # Resposta em texto simples

# Configuração do servidor
server_address = ('localhost', 8080)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print("Servidor rodando em http://localhost:8080")
httpd.serve_forever()