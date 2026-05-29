import json
import os

arquivo = 'pacientes.json'

print(' Sistema de Cadastro de Pacientes '.center(50, '-'))
print()

#carregar dados do arquivo (se existir)
def carregar_dados():
    if not os.path.exists(arquivo):
        return []
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f) #validação simples.
            if isinstance(dados, list):
                return dados
            else:
                print('⚠Formato do arquivo inválido. Iniciando com lista vazia.')
                return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"⚠Erro ao carregar dados '{arquivo}': {e}. Iniciando com lista vazia.")
        return []
    
#salvar dados no arquivo
def salvar_dados(pacientes):    
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(pacientes, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"⚠Erro ao salvar dados em '{arquivo}': {e}.")

#lista principal (carregada do arquivo)
pacientes = carregar_dados()

def cadastrar_paciente():
    print(' \n===CADASTRAR PACIENTE=== ')
    try:
        nome = input('Nome do paciente: ').strip()
        if not nome:
            print('⚠Nome não pode ser vazio.')
            return
        idade_input = int(input('Idade: ').strip())
        idade = int(idade_input) #pode lançar ValueError)
        telefone = input('telefone: ').strip()
        paciente = {'nome': nome, 'idade': idade, 'telefone': telefone}
        pacientes.append(paciente)
        salvar_dados(pacientes) #salvar imediatemente após o cadastro
        print(f"✅Paciente '{nome}' cadastrado com sucesso!")
        execpt ValueError:
        print('⚠Idade inválida. Digite um número inteiro.\n')

def ver_estatisticas():
    print(' \n===ESTATÍSTICAS DOS PACIENTES=== ')
       if not pacientes:
        print('Nenhum paciente cadastrado.')
        return
    total = len(pacientes)
    idades = [p['idade'] for p in pacientes]
    media = sum(idades) / total
    mais_novo = min(pacientes, key=lambda p: p['idade'])
    mais_velho = max(pacientes, key=lambda p: p['idade'])
    print(f'🚻Total de pacientes: {total}')
    print(f'📊Idade média: {media:.2f} anos')
    print(f'👶Paciente mais novo: {mais_novo["nome"]} ({mais_novo["idade"]} anos)')
    print(f'👴Paciente mais velho: {mais_velho["nome"]} ({mais_velho["idade"]} anos)')




        
  