from cep import BuscaEndereco
import requests as rq
# cadastro = Datas()

# print(cadastro.dia_semana())
cep = 88034001
hoje = BuscaEndereco(cep)


a = hoje.acessa_api_viacep()

print(a)