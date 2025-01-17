"""
Ciência da Computação - 3º Semestre

1. Terceira verificação de aprendizagem (projeto).
2. Instruções do desenvolvimento do projeto para avaliação:
- Fazer em grupo de até cinco pessoas, mas a apresentação será individual.
- Prazo: enviar dia 16/06/20 até 16h.
- Apresentação: dia 17/06/20 no Google Meet no horário da aula.
- Coloque o nome de todos os alunos do grupo dentro de cada programa ‘.py’
- Apenas um aluno do grupo deve enviar o projeto pela atividade do Classroom em um arquivo
“.zip” (aluno1_aluno2_aluno3_aluno4.zip) com todos os arquivos desenvolvidos:
Um arquivo projeto1 “.py”; e
Um arquivo projeto2 “.py”.
3. Projeto 1 (POO):
Elabore o enunciado de um problema que será resolvido com POO, herança e classe abstrata.
O projeto deve ter no mínimo:
- Uma superclasse abstrata OK
- Duas subclasses OK
- Atributos de instância e atributos de classe
- Alguns métodos gets, sets e pelo menos seis métodos funcionais OK
- Métodos sobrescritos OK
- Métodos de classe OK
- Métodos concretos e métodos abstratos OK
- Programa principal (método main) criando objetos e usando os métodos das classes. OK
- Listas OK
"""
from abc import ABC, abstractmethod
import random
class User(ABC):
    @abstractmethod
    def Login(self):
        pass
class Paciente(User):
    def __init__(self,login,senha,nome,endereco=None,registros=0):
        self.login=login
        self.senha=senha
        self.nome=nome
        self.exame=list()
        self.endereco=endereco
        self.registros=registros
        self.log=False
    def __str__(self):
        s=f"Informações do paciente: {self.nome}\nLogin:{self.login}\nEndereço atual: {self.endereco}"
        return s
    def Login(self): #1
        tentativa=0
        while tentativa<=3:
            login=str(input("Digite o seu CPF: "))
            if len(login)>11 or len(login)<11 or len(login)==0:
                print("CPF inválido")
                tentativa+=1
                continue
            senha=str(input("Digite a sua senha: "))
            if len(senha)==0:
                print("Senha inválida")
                tentativa+=1
                continue
            if str(self.login)==str(login) and str(self.senha)==str(senha):
                self.log=True
                print("\nLogin realizado com sucesso\n")
                return self.log
            else:
                print("\nDado Inválido, tente novamente\n")
                tentativa+=1 
        else:
            print("Número de tentativas excedido, encerrando sessão\n")
            self.log=False
            return self.log
    def logout(self): #2
        while self.log==True:
            op = str(input("Você deseja sair?\n[Y]/[N]\n")).upper()
            if op=="Y":
                print("Logout realizado com sucesso")
                self.log = False
                break
            elif op=="N":
                print("Logout cancelado")
                break
            else:
                print("Opção inválida")
        else:
            print("Login não realizado")
    def get_nome(self):
        return self.nome
    def get_log(self):
        return self.log
    def get_endereco(self):
        return self.endereco
    def set_endereco(self,new):
        self.endereco = new
    def get_exame(self):
        return self.exame
    def set_nome(self,new):
        self.nome = new
    def marcar_exame(self): #3
        print(f"Olá, {self.nome}\nPainel De Marcação de Exame")
        tipo = input("Tipo do Exame: ")
        data = input("\nInsira a data(aaaa-mm-dd): ")
        medico = input("\nInsira o nome Médico: ")
        marcado=[tipo,data,medico]
        self.exame.append(marcado)
        self.registros+=1
    def ver_exame(self): #4
        i=0
        if len(self.exame)>0:
            print(f"Histórico de exames do paciente {self.nome}:")
            while i<self.registros:
                print("\n--------------------------------")
                print(f"Exame nº{i+1}")
                print("Tipo de exame:",self.exame[i][0])
                print("\nData do exame:",self.exame[i][1])
                print("\nMédico responsável pelo exame:",self.exame[i][2])
                print("\n--------------------------------")
                i+=1
            print("\n")
        else:
            print("Nenhum exame marcado")
    def cancelar_exame(self): #5
        Paciente.ver_exame(self)
        op=int(input("Selecione, da lista, o nº do exame que deseja remover:\n"))
        confirm=self.exame[op-1]
        while True:
            confmesg=input(f"Deseja cancelar {confirm}?\n[Y]/[N]\n").upper()
            if confmesg=="Y":
                self.exame.pop(op-1)
                print("Operação concluída")
                break
            elif confmesg=="N":
                print("Operação cancelada")
                break
            else:
                print("Opção inválida")
    def remarcar_exame(self): #6
        Paciente.ver_exame(self)
        op=int(input("Selecione, da lista, o nº do exame que deseja remarcar:\n"))
        confirm=self.exame[op-1]
        while True:
            confmesg=input(f"Deseja remarcar {confirm}?\n[Y]/[N]\n").upper()
            if confmesg=="Y":
                newDate=input("Digite a nova data(aaaa-mm-dd):\n")
                self.exame[op-1][1]=newDate
                print(self.exame[op-1])
                print("Operação concluída")
                break
            elif confmesg=="N":
                print("Operação cancelada")
                break
            else:
                print("Opção inválida")
class Medico(Paciente):
    def __init__(self,login,senha,nome,especialidade):
        super().__init__(login,senha,nome)
        self.especialidade = especialidade
        self.log=False
    def Login(self): #1
        tentativa=0
        while tentativa<=3:
            login=str(input("Digite o seu CRM: "))
            if len(login)==0:
                print("CRM inválido")
                tentativa+=1
                continue
            senha=str(input("Digite a sua senha: "))
            if len(senha)==0:
                print("Senha inválida")
                tentativa+=1
                continue
            if str(self.login)==str(login) and str(self.senha)==str(senha):
                self.log=True
                print("\nLogin realizado com sucesso\n")
                return self.log
            else:
                print("\nDado Inválido, tente novamente\n")
                tentativa+=1 
        else:
            print("Número de tentativas excedido, encerrando sessão\n")
            self.log=False
            return self.log
    def logout(self): #2
        while self.log==True:
            op = str(input("Você deseja sair?\n[Y]/[N]\n")).upper()
            if op=="Y":
                print("Logout realizado com sucesso")
                self.log = False
                break
            elif op=="N":
                print("Logout cancelado")
                break
            else:
                print("Opção inválida")
        else:
            print("Login não realizado")
    def get_nome(self):
        return self.nome
    def get_crm(self):
        return self.login
    def num_consultas(self,pac):
        #O objetivo da função é retornar o número de consultas que um paciente já realizou ou irá realizar com um determinado médico
        con=Paciente.get_exame(pac) #Armazena a lista de exames de um paciente em uma variável local
        search=0 #Contador
        found=[] #Lista para dos exames que pertencem ao médico em questão, feito para printar a lista de todos os exames
        while True:
            if search in con:
                found.append(con[search])
                con.pop[search]
            else:
                if search==(len(con)+1):
                    break
                else:
                    search+=1
        print(f"Consultas marcadas com o paciente {Paciente.get_nome(pac)}: {search-1}")
        i=0
        while i < len(found):
            print("Tipo de exame:",found[i][0])
            print("\nData do exame:",found[i][1])
            i+=1
    def registra_paciente(self):
        while True:
            cpf=int(input("Digite o CPF do paciente:\n"))
            if len(str(cpf))<11 or len(str(cpf))>11 or len(str(cpf))==0:
                print("CPF inválido")
                continue
            name=input("Digite o nome do paciente:\n")
            if len(name)==0:
                print("Nome inválido")
                continue
            end=input("Digite o endereço do paciente:\n")
            if len(end)==0:
                print("Endereço inválido")
                continue
            presenha=[]
            for i in range(6):
                if i==6:
                    break
                a=random.randint(0,9)
                presenha.append(a)
                i+=1
                conversor = [str(presenha) for presenha in presenha]
                converter = "".join(conversor)
                senha = int(converter)
            print(f"Informe a seguinte senha para o seu paciente e peça-o para guardar-la com segurança\nSenha: {senha}")
            return Paciente(cpf,senha,name,end)
if __name__ == "__main__":
    #Login do CLIENTE é o CPF
    #Login do MEDICO é o CRM
    p1=Paciente(12345678912,112233,"João Azevedo","apt 404, Edifício Araucárias, QR410, Brasilia, DF")
    m1=Medico(45678,122456,"Carlos Almeida","Pediatra")
    while True:
        print("Bem-vindo ao sistema do Hospital Público de Brasília\nDigite [0] em qualquer um dos menus para encerrar a sessão\n")
        inicio=int(input("Você é um:\n[1]Paciente\n[2]Médico\n"))
        if inicio==1:
            login=Paciente.Login(p1)
            while login==True:
                menu=int(input("Selecione uma das opções:\n[1] - Ver histórico de exames\n[2] - Marcar exame\n[3] - Cancelar exame\n[4] - Remarcar exame\n[0] - Fazer logout\n"))
                if menu==1:
                    p1.ver_exame()
                    continue
                elif menu==2:
                    p1.marcar_exame()
                    continue
                elif menu==3:
                    p1.cancelar_exame()
                    continue
                elif menu==4:
                    p1.remarcar_exame()
                    continue
                elif menu==0:
                    p1.logout()
                    break
                else:
                    print("Opção inválida")
            else:
                continue
        elif inicio==2:
            login=Medico.Login(m1)
            while login==True:
                menu=int(input("Selecione uma das opções:\n[1] - Ver consultas com um determinado paciente\n[2] - Marcar exame\n[3] - Cadastrar paciente\n[0] - Fazer logout\n"))
                if menu==1:
                    m1.num_consultas(p1)
                elif menu==2:
                    print(f"Agendando exame para {p1.get_nome()}\n")
                    p1.marcar_exame()
                elif menu==3:
                    c2=m1.registra_paciente()
                elif menu==0:
                    m1.logout()
                    break
                else:
                    print("Opção inválida")
        elif inicio==0:
            print("Sessão encerrada")
            break
        else:
            print("Opção inválida")