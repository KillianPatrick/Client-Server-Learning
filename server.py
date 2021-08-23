from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime

server = SimpleXMLRPCServer(('localhost', XXXXXX), logRequests = True)

def verifica_Operacao(op):
    if op == 1:
        dia = datetime.today()
        print('DATA DE HOJE', dia)
        hoje = dia.strftime("%m/%d/%Y")
        return str.encode(hoje)
    if op == 2:
        hora = datetime.now()
        print('A HORA AGORA', hora)
        agora = hora.strftime("%H:%M:%S")
        return str.encode(agora)


server.register_function(verifica_Operacao)
print("Server on...")

server.serve_forever()
