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
    