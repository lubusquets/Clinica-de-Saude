#  :hospital: Projeto Integrado Inovação - Clínica Vida+

> Sistema acadêmico desenvolvido em Python para gestão de pacientes, aplicando Scrum, JSON, Álgebra Booleana, UML e Engenharia de Software.

Desenvolvido no segundo semestre do curso de Análise e Desenvolvimento de Sistemas, o projeto tem como objetivo demonstrar a aplicação prática dos conhecimentos adquiridos ao longo do semestre por meio da criação de uma solução tecnológica para a gestão de uma clínica médica, integrando conceitos de programação, engenharia de software, gestão de projetos e modelagem de sistemas.

# :rocket: Funcionalidades

- :white_check_mark: Cadastro de pacientes
- :mag: Busca de pacientes por nome
- :clipboard: Listagem completa de registros
- :bar_chart: Estatísticas dos pacientes cadastrados
- :floppy_disk: Persistência de dados utilizando JSON
- :brain: Controle de acesso com Álgebra Booleana
- :memo: Algoritmo em pseudocódigo para gerenciamento de filas
- :chart_with_upwards_trend: Gestão do projeto utilizando Scrum e Trello
- :dart: Modelagem UML com Diagrama de Casos de Uso

# :hammer_and_wrench: Tecnologias Utilizadas

| Tecnologia | Aplicação |
|---|---|
|:snake: Python	| Desenvolvimento do sistema|
|:page_facing_up: JSON	| Armazenamento persistente dos dados|
|:clipboard: Scrum	| Gerenciamento ágil do projeto|
|:pushpin: Trello	| Organização das Sprints|
|:brain: Lógica Booleana	| Controle de acesso|
|:triangular_ruler: UML	Modelagem de | Casos de Uso|
|:pencil2: Pseudocódigo	| Simulação de fila de atendimento|

# :bar_chart: Gestão do Projeto com Scrum e Trello

Para o planejamento e acompanhamento das atividades, foi utilizada a metodologia **Scrum**, com apoio da ferramenta **Trello** para o gerenciamento das tarefas e das Sprints.

O quadro foi organizado em etapas que representam o fluxo de desenvolvimento do projeto, permitindo acompanhar a evolução das atividades desde o levantamento dos requisitos até a entrega final.

Essa abordagem proporcionou maior controle sobre o andamento do projeto, melhor organização das demandas e acompanhamento contínuo da evolução do sistema.



**Fluxo de Trabalho:**

1. **Backlog** – Organização dos requisitos e critérios de aceitação.
2. **Sprint Atual** – Atividades planejadas para o ciclo de desenvolvimento.
3. **Em Progresso** – Funcionalidades em desenvolvimento.
4. **Teste** – Validação das funcionalidades e coleta de feedback dos usuários.
5. **Concluído** – Tarefas finalizadas e entregues.



# :closed_lock_with_key: Sistema de Controle de Acesso Automático
*Tabelas verdade criadas para este projeto.*

Nesta primeira tabela - **Tabela Verdade para Consulta Normal (CN = V)** - o paciente pode ser atendido em 3 situações diferentes que são as células marcadas em azul claro.

![Error](https://github.com/lubusquets/Clinica-de-Saude/blob/main/img/Tabela1.jpeg?raw=true)

Na segunda tabela - **Tabela Verdade para Consulta de Emergencia (E = V)** - o paciente pode ser atendido em 6 situações diferentes . Células também marcadas em azul claro.

![Error](https://github.com/lubusquets/Clinica-de-Saude/blob/main/img/Tabela2.jpeg?raw=true)

***Explicando as tabelas acima:**

Se um paciente chega com as seguintes condições, ele será atendido?

1. Sem agendamento (A = F)
2. Documentos OK (B = V)
3. Médico disponível (C = V)
4. Pagamentos atrasados (D = F)

Levando em consideração as premissas informadas acima, para Consulta Normal - expressão: **CN=(A∧B∧C)∨(B∧C∧D)** - nós temos os seguintes resultados:
Substituindo:

**Primeiro grupo: F ∧ V ∧ V = F**

**Segundo grupo: V ∧ V ∧ F = F**

:x: Nesta situação o paciente não será atendido para consulta normal.

Para Consulta de Emergência - expressão: **E=C∧(B∨D)** - temos:

Substituindo:

Primeiro grupo: C = V

Segundo grupo: V ∨ F = V

:white_check_mark: Sendo assim **V ∧ V = V**, nesta situação o paciente será atendido na emergência.

# :busts_in_silhouette: Diagrama de Casos de Uso e Relacionamentos

**Regras utilizadas:** 

-	Agendamento e Confirmação exigem que o paciente esteja cadastrado (relação include).
- Cancelamento é realizado apenas pelo médico.
-	Toda vez que uma receita é gerada, o sistema dispara automaticamente a impressão (relação extend).


![Error](https://github.com/lubusquets/Clinica-de-Saude/blob/main/img/casos-de-uso.jpeg?raw=true)

# :clipboard: Competências Desenvolvidas

**:computer: Programação**
- Python
- Funções
- Listas
- Dicionários

**:floppy_disk: Persistência de Dados**
- JSON

**:clipboard: Engenharia de Software**
- Scrum
- Backlog
- Sprints

**:brain: Lógica Computacional**
- Álgebra Booleana
- Tabelas Verdade

**:triangular_ruler: Modelagem**
- UML
- Pseudocódigo


