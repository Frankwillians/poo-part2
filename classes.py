from pilha import PilhaEncadeada
from lista import ListaEncadeada
from fila import Fila

#Classe Advogado

class Advogado:
    def __init__(self,cod_oab,nome,processos):
        self._cod_oab = cod_oab
        self._nome = nome
        self._processos = processos
        self._processosL = ListaEncadeada()
        self._processosP = PilhaEncadeada()
        self._processosF = Fila()

    #gets
    @property
    def processosL(self):
        return self._processosL
    @processosL.setter
    def processosL(self,novo):
        self._processosL = novo
    
    @property
    def processosF(self):
        return self._processosF
    
    @processosF.setter
    def processosF(self,novo):
        self._processosF = novo
    
    @property
    def processosP(self):
        return self._processosP
    @processosP.setter
    def processosP(self,novo):
        self._processosP = novo        




    def get_cod_oab(self):
        return self._cod_oab

    def get_nome(self):
        return self._nome

    
    def get_processos(self):
        return self._processos 
    
    #sets
    
    
    def set_cod_oab(self,novo_cod):
        self._cod_oab = novo_cod


    def set_nome(self,novo_nome):
        self._nome = novo_nome

    def set_processos(self,novos_processos):
        self._processos = novos_processos   
  

    #metodos
    def maior_custo(self):
       
        for i in range(len(self._processosL)):
            for c in range(i):

                if self._processosL[i]._custo > self._processosL[c]._custo:
                    return f'Status: {self._processosL[i]._status}, code: {self._processosL[i]._cod}'
                else:
                    return f'Status: {self._processosL[c]._status}, code: {self._processosL[c]._cod}'
      
    def menor_custo(self):
       
        for i in range(len(self._processosL)):
            for c in range(i):

                if self._processosL[i]._custo < self._processosL[c]._custo:
                    return f'Status: {self._processosL[i]._status}, code: {self._processosL[i]._cod}'
                else:
                    return f'Status: {self._processosL[c]._status}, code: {self._processosL[c]._cod}'
      
                 
    def incrementa_custo(self,cod,valor):
        for c in range(len(self._processosL)):
            if cod == self._processosL[c]._cod:
                 self._processosL[c]._custo += valor
    def adicionar_processo_P(self,novo):
        self._processosP = novo

    def lista_clientes(self):
        clientes = []
        for i in range(len(self._processos)):
            if self._processos[i]._pessoa not in clientes:
                    clientes.append(self._processos[i].get_pessoa()) 
        for i in range(len(clientes)):
            return(clientes[i])


    def __str__(self):
        return f'Nome: {self._nome}, codigo OAB: {self._cod_oab}'       

#Classe Audiencia

class Audiencia:
    def __init__ (self,data,recomendacao,duracao):
        self._data = data
        self._recomendacao = recomendacao
        self._duracao = duracao
 
    #getters
    
    def get_data(self):
        return self._data
    
    def get_recomendacao(self):
        return self._recomendacao    
    
    def get_duracao(self):
        return self._duracao

   
    
    #setters

    def set_data(self,nova_data):
        self._data = nova_data
    

    def set_recomendacao(self,nova_recomendacao):
        self._recomendacao = nova_recomendacao    
    
    
    def set_duracao(self,nova_duracao):
        self._duracao = nova_duracao
    


    

    def __str__ (self):
        return f'realizada na data de: {self._data}, recomendação {self._recomendacao}, e teve duração de {self._duracao} min'        


#Classe Custo

class Custo:
    def __init__(self,data,descricao,valor):
        self._data = data
        self._descricao = descricao
        self._valor = valor
   
   #getters
    @property
    def data(self):
       return self._data

    @property
    def descricao(self):
        return self._descricao

    @property
    def valor(self):
        return self._valor

    #setters     
    
    @data.setter
    def data(self,nova_data):
        self._data = nova_data

    @descricao.setter
    def descricao(self,nova_desc):
        self._descricao = nova_desc

    @valor.setter
    def valor(self,novo_valor):
        self._valor = novo_valor       


#Classe Pessoa

class Pessoa:
    def __init__(self, cpf, nome, processos = []):
        self._cpf = cpf
        self._nome = nome
        self._processos = processos

        
   #getters
       

    
    def get_cpf(self):
       return self._cpf
    
    def get_nome(self):
        return self._nome
    
    def get_processos(self):
        return self._processos
    
    #setters

    
    def set_cpf(self,novo_cpf):
       self._cpf = novo_cpf
    
    def set_nome(self,novo_nome):
        self._nome = novo_nome
    
  
    def set_processos(self,novos_processos):
        self._processos = novos_processos       

    
    #metodos 

    def num_descisoes(self,dec):
        if dec == 'True':
            defer = 0
            for i in range(len(self._processos)):
                if self._processos[i].get_decisao() == True:
                    defer += 1
            return defer
        elif dec == 'False':
            indef = 0
            for i in range(len(self._processos)):
                if self._processos[i].get_decisao() == False:
                    indef += 1             
            return indef

    def custo_total(self):
        custo = 0
        for i in range(len(self._processos)):
            custo += self._processos[i].get_custo()
        return custo    
    def custo(self):
        procs_custos = []
        for i in range(len(self._processos)):
            procs_custos.append(self._processos[i])    
    def custo_total_adv(self,cod_oab):
        adv_custo = 0
        for i in range (len(self._processos)):
            if self._processos[i]._advogado._cod_oab == cod_oab:
                adv_custo += self._processos[i].get_custo()
                
        return adv_custo 
    
    def processos_cliente(self):
       lista = []
       for i in range(len(self._processos)):
           lista.append(self._processos[i])
       return lista

  


    def __str__(self):
        return f'Cliente: {self._nome}, de CPF: {self._cpf}'


#Classe Processo

class Processo:
    def __init__(self,descricao,custo,decisao,status,pessoa,advogado,audiencias,cod):
        self._descricao = descricao
        self._custo = custo
        self._decisao = decisao
        self._status = status
        self._pessoa = pessoa
        self._advogado = advogado
        self._audiencias = audiencias
        self._cod = cod
        self._prox = None
  
    
    #geters
    def get_decisao(self):
        if self._decisao == 'defer':
            return True
        elif self._decisao == 'indef':
            return False    
    
    def get_status(self):
        return self._status
    
    def get_pessoa(self):
        return self._pessoa

    def get_advogado(self):
        return self._advogado
    
    def get_audiencias(self):
        return self._audiencias  
    def get_custo(self):
        return self._custo               

    #setters
    def set_status(self,novo):
         self._status = novo

    def set_custo(self,novo):
        self._custo = novo  

    def set_audiencias(self,nova):
        self._audiencias = nova

    def set_decisao(self,novo):
        self._decisao = novo
    def set_advogado (self,novo):
        self._advogado = novo
    def set_pessoa(self,nova):
        self._pessoa = nova    

    #metodos 

    def audiencias_temp(self,tempo):
        for i in range (len(self._audiencias)):
            if self._audiencias[i].get_duracao() >= tempo:
                print(self._audiencias[i])
        return ''    

    def total_horas(self):
        total = 0
        for i in range(len(self._audiencias)):
            total += self._audiencias[i].get_duracao()
        return total    


    def __str__(self):
        return f'{self._descricao}'
            

