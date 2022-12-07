from cep import BuscaEndereco
# cadastro = Datas()

# print(cadastro.dia_semana())
cep = 81750240
hoje = BuscaEndereco(cep)


a = hoje.acessa_api_viacep()

print(a)