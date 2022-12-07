from Cpf_cnpj import Documento
from validate_docbr import CNPJ

cpf = '03807399097'

obj_cpf = Documento.cria_doc(cpf)

print(obj_cpf)


# ex_cnpj = '80150857000127'
# cnpj = Documento.cria_doc(ex_cnpj)
# print(cnpj)

