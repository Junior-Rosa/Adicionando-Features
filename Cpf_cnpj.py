from validate_docbr import CPF
from validate_docbr import CNPJ


class Documento:
    
    @staticmethod
    def cria_doc(doc):
        if len(doc) == 11:
            return DocCpf(doc)
        elif len(doc) == 14:
            return DocCnpj(doc)
        else:
            raise ValueError("Quantidade de digitos incorreta!!")

class DocCpf:
    def __init__(self, doc) -> None:
        if self.valida(doc):
            self.cpf = doc
        else:
            raise ValueError("CPF inválido!!")
    
    def __str__(self) -> str:
        return self.format()
        
    def valida(self,doc):
        validador = CPF()
        return validador.validate(doc)
        
    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    
    def __init__(self,doc) -> None:
        if self.valida(doc):
           self.cnpj = doc
        else:
            raise ValueError("CNPJ inválido!!")
        
    def __str__(self) -> str:
        return self.format()
    
    def valida(self,doc):
        validador = CNPJ()
        return validador.validate(doc)
        
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    





class CpfCnpj:
    
    def __init__(self, documento, tipo_doc) -> None:
        self.tipo_doc = tipo_doc
        documento = str(documento)
        if tipo_doc == 'cpf':
            if self.cpf_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF INVALIDO!!")
        elif self.tipo_doc == 'cnpj':
            if self.cnpj_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError('CNPJ Invalido!')
            
    def __str__(self) -> str:
        
        if self.tipo_doc == 'cpf':
            return self.format_cpf()
        if self.tipo_doc == 'cnpj':
            return self.format_cnpj()

    def cpf_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError('Quantidade de digitos inválida!')

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    
    def cnpj_valido(self, cnpj):
        if len(cnpj) == 14:
            valida_cnpj = CNPJ()
            return valida_cnpj.validate(cnpj)
        else:
            raise ValueError('Quantidade de digitos inválida!')