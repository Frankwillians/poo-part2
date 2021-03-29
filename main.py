from classes import Processo
from classes import Pessoa
from classes import Advogado
from classes import Custo
from classes import Audiencia
proc_exec = []
proc_exec2 = []
lista_adv = []
lista_pess = []
proc_marcus = []
proc_francis = []
lista_time_pess1 = []
lista_time_pess2 = []
lista_geral = [ ]


#custos 

custo1 = Custo('21/09/21','roubo',25400) #5698
custo2 = Custo('21/09/21','estelionato',600) #2569
custo3 = Custo('21/09/21','roubo de carro',750)

# pessoas: 
pess_1 = Pessoa('123.405.454-53','Carlos',proc_exec)
pess_2 = Pessoa('143.604.265-92','Maria',proc_exec2)


lista_pess.append(pess_1)
lista_pess.append(pess_2)

#advogados:
adv1 = Advogado('25698','Marcus',proc_marcus)
lista_adv.append(adv1)
proc_francis = []
adv2 = Advogado('29788','Francis',proc_francis)
lista_adv.append(adv2)
#lista de audiencias por processo
#processo 1 :
lista_aud = []

aud1 = Audiencia('27/08/2021','nenhuma',60)
aud2 = Audiencia('28/09/2021','nenhuma',90)
aud3 = Audiencia('25/12/2021','nenhuma',45)

lista_aud.append(aud1)
lista_aud.append(aud2)
lista_aud.append(aud3)

#processo 2:

lista_aud2 = []
aud4 = Audiencia('27/08/2021','nenhuma',90)
aud5 = Audiencia('28/09/2021','nenhuma',30)
lista_aud2.append(aud4)
lista_aud2.append(aud5)

#processo 3:
lista_aud3 = []
aud6 = Audiencia('27/08/2021','nenhuma',90)
aud7 = Audiencia('28/09/2021','nenhuma',30)
aud8 = Audiencia('28/09/2021','nenhuma',40)
lista_aud3.append(aud6)
lista_aud3.append(aud7)
lista_aud3.append(aud8)

#criação de processos:
#processo 1:
process_1 = Processo('roubo',custo1.valor,'indef','andamento',pess_1,adv1,lista_aud,5698)
proc_exec.append(process_1)
lista_geral.append(process_1)
lista_time_pess1.append(process_1)

#setando no processo 1:
process_1.set_audiencias(lista_aud)



#processo 2:
process_2 = Processo('estelionato',custo2.valor,'defer','andamento',pess_1,adv1,lista_aud2,2569)
proc_exec.append(process_2)
proc_marcus.append(process_2)
lista_geral.append(process_2)
lista_time_pess1.append(process_2)
#setando no processo 2:
process_2.set_audiencias(lista_aud2)


#processo 3:
process_3 = Processo('roubo de carro',custo3.valor,'defer','encerrada',pess_2,adv2,lista_aud3,4589)
proc_exec2.append(process_3)
proc_francis.append(process_3)
lista_geral.append(process_3)
lista_time_pess2.append(process_3)
#setando no processo 3:
process_3.set_audiencias(lista_aud3)


#setando processos:
pess_1.set_processos(proc_exec)
pess_2.set_processos(proc_exec2)

#setando advogados: 
adv1.set_processos(proc_marcus)
adv2.set_processos(proc_francis)

adv1._processosL.append(process_1)
adv1._processosL.append(process_2)
adv2._processosF.add(process_3)

print(adv1.menor_custo())
print(adv1._processosL[1]._custo)
adv1.incrementa_custo(2569,550)
print()
print(adv1._processosL[1]._custo)