from datetime import datetime, timedelta


class Datas:
    
    def __init__(self) -> None:
        self.momento_cadastro = datetime.today()
        
    def __str__(self) -> str:
        return self.format()
        
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
    
    def format(self):
        data_formatada = self.momento_cadastro.strftime(r'%d/%m/%Y %H:%M')
        return data_formatada
    
    def tempo_cadastro(self):
        tempo = datetime.today() - self.momento_cadastro
        return tempo
    