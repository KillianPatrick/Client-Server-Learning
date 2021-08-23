from xmlrpc.client import ServerProxy


proxy = ServerProxy('http://localhost:XXXXX')
while True:
    print('\nPara verificar data digite: 1')
    print('Para verificar hora digite: 2')
    operacao = int(input())
    op = operacao

    resposta = proxy.verifica_Operacao(op)

    print('Resposta do servidor:', resposta)

