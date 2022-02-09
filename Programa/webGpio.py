#webGpio.py
#  www.ea7tb.com
"""
conmutador de antena.
procesa la entrada de pulsaciones en una pagina web.
puede actuar hasta 5 reles.
Las salidas a pantalla desactivados.
Falta seguridad
"""
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
from pyA20.gpio import gpio
from pyA20.gpio import port

rele_1 = port.PA18
rele_2 = port.PA11
rele_3 = port.PA12
rele_4 = port.PA19
rele_5 = port.PA14

gpio.init()
gpio.setcfg(rele_1, gpio.OUTPUT)
gpio.setcfg(rele_2, gpio.OUTPUT)
gpio.setcfg(rele_3, gpio.OUTPUT)
gpio.setcfg(rele_4, gpio.OUTPUT)
gpio.setcfg(rele_5, gpio.OUTPUT)

host_name = '192.168.1.175'    # Change this to your Raspberry Pi IP address
host_port = 8000
def apagado():
    gpio.output(rele_1, 1)
    gpio.output(rele_2, 1)
    gpio.output(rele_3, 1)
    gpio.output(rele_4, 1)
    gpio.output(rele_5, 1)


class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Orange Pi
    """
    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command
            'curl -I http://server-ip-address:port'
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """
        html = '''
            <html>

            <body style="width:960px; margin: 20px auto;">
            <h1>Conmutador de Antenas</h1>
            <p>Antena 1: <a href="/on_1">On</a> <a href="/off_1">Off</a></p>
            <p>Antena 2: <a href="/on_2">On</a> <a href="/off_2">Off</a></p>
            <p>Antena 3: <a href="/on_3">On</a> <a href="/off_3">Off</a></p>
            <p>Antena 4: <a href="/on_4">On</a> <a href="/off_4">Off</a></p>
            <p>Antena 5: <a href="/on_5">On</a> <a href="/off_5">Off</a></p>

            <div id="led-status"></div>
            <script>
                document.getElementById("led-status").innerHTML="{}";
            </script>
            </body>
            </html>
        '''
        temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        self.do_HEAD()
        status = ''
        if self.path=='/':
            # GPIO.setmode(GPIO.BCM)
            # GPIO.setwarnings(False)
            #GPIO.setup(18, GPIO.OUT)
            print ("/")
        elif self.path=='/on_1':
            apagado()
            gpio.output(rele_1, 0)
            status='Antena 1 Activa'
        elif self.path=='/off_1':
            gpio.output(rele_1, 1)
            status='Antena 1 Desactivada'

        elif self.path=='/on_2':
            apagado()
            gpio.output(rele_2, 0)
            status='Antena 2 Activa'
        elif self.path=='/off_2':
            gpio.output(rele_2, 1)
            status='Antena 2 Desactivada'

        elif self.path=='/on_3':
            apagado()
            gpio.output(rele_3, 0)
            status='Antena 3 Activa'
        elif self.path=='/off_3':
            gpio.output(rele_3, 1)
            status='Antena 3 Desactivada'

        elif self.path=='/on_4':
            apagado()
            gpio.output(rele_4, 0)
            status='Antena 4 Activa'
        elif self.path=='/off_4':
            gpio.output(rele_4, 1)
            status='Antena 4 Desactivada'

        elif self.path=='/on_5':
            apagado()
            gpio.output(rele_5, 0)
            status='Antena 5 Activa'
        elif self.path=='/off_5':
            gpio.output(rele_5, 1)
            status='Antena 5 Desactivada'


        self.wfile.write(html.format(temp[5:], status).encode("utf-8"))
if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    # desactivado print, solo para control
    #print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()

