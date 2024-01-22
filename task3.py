import socket
servername = "www.fongen.no"
serverport = 80
# Merk den tomme linja (før slutt-""") som genererer en ekstra <CR><LF> etter HTTP-header
request = """
GET /ing1506/getweb.html HTTP/1.1
Host: {host}
Connection: close

""".format(host=servername)
# Inspeksjon av strengvariabel mtp. Feilsøking:
#print(request)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((servername, serverport))
clientSocket.send(request.encode())
response = clientSocket.recv(20000)
clientSocket.close()
print(response.decode())
