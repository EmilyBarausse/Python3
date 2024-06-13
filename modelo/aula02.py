# POLIMORFISMO

class Programa:
    
    def __init__(self,nome,ano):
        self._nome=nome.title()
        self.ano=ano
        self._likes = 0
        
    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes+=1
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter 
    def nome(self,nome):
        self._nome=nome
        
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self._likes} likes')
       
       
class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao=duracao 
        
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes')

        
class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self.temporadas=temporadas
        
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} likes')
        
        
filme1=Filme('Star Wars', 1977, 132)
filme1.dar_likes()
filme1.dar_likes()
# print(f'Nome: {filme1.nome} | Ano: {filme1.ano} | Duração: {filme1.duracao} | Likes: {filme1.likes}')
# print('')

serie1=Serie('Greys Anatomy',2005, 20)
serie1.dar_likes()
serie1.dar_likes()
serie1.dar_likes()
# print(f'Nome: {serie1.nome} | Ano: {serie1.ano} | Temporadas: {serie1.temporadas} | Likes: {serie1.likes}')
# print('')

# 1 criando um list para armazenas os objetos

filmes_e_series=[filme1,serie1]

# 2 escrever um if que verifica dentro do for se cada iteração possui determinado atributo
# for programa in filmes_e_series:
#     detalhes=programa.duracao if hasattr(programa,'duracao') else programa.temporadas
#     print(f'{programa.nome} - {programa.ano} - {detalhes} - {programa.likes} likes') 
#     print('')

for programa in filmes_e_series:
    programa.imprime()