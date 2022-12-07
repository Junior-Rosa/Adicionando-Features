from datetime import datetime, timedelta


class Datas:
    
    def __init__(self) -> None:
        self.momento_cadastro = datetime.today()
        
    def mes(self):
        meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
        mes_cadastro = self.momento_cadastro.month -1
        return meses[mes_cadastro]
    
    def dia_semana(self):
        semana =(
            'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo'
        )
        dia_semana = self.momento_cadastro.weekday() 
        return semana[dia_semana]