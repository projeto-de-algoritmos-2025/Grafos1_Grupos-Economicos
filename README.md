# Grafos 1 - Grupos Econômicos

**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos 1 - BFS, DFS<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/2046229  |  Kallyne Macêdo Passos |
| 20/0022199  | Leonardo Sobrinho de Aguiar |

## Sobre 
O projeto aplica algoritmos de grafos para analisar e visualizar redes de relacionamentos empresariais. Utiliza-se a busca por profundidade (DFS) para a identificação de componentes conectados, que representam diferentes grupos econômicos e se calcula o grau de centralidade para definir as principais empresas presentes nesses grupos. A busca por largura (BFS) é utilizada para detectar ciclos e realizar a ordenação topológica em grafos direcionados, criando as hierarquias de controle entre as companhias.  

Um grupo econômico consiste em um conjunto de empresas, e o grafo que o representa depende da natureza da relação entre elas. Se a relação for de parceria, o grafo é não direcionado, pois as empresas mantêm vínculos mútuos. Já em uma relação de controle, o grafo deve ser direcionado, uma vez que uma empresa tem impacto direto nas decisões da outra. Dessa forma, é possível realizar um estudo visual das interações empresariais, o que facilita a compreensão dessas dinâmicas e a melhor visualização do impacto que elas causam.

## Screenshots
<center>Grafo do Grupo 10</center>
<img width="1521" height="810" alt="Grafo10" src="https://github.com/user-attachments/assets/ae3d178a-45ec-472a-bd4b-c41c0f0923d9" />
<center>Grafo direcionado demonstra a relação do Grupo 10 e sua ordenação topológica</center>
<br>
<center>Grafo do Grupo 9</center>
<img width="1513" height="810" alt="Grafo9" src="https://github.com/user-attachments/assets/345fa283-9caf-477c-b89b-d267f03cd117" />
<center>Grafo direcionado demonstra a relação do Grupo 9 e sua ordenação topológica</center>
<br>
<center>Grafo do Grupo 8</center>
<img width="1524" height="822" alt="Graffo8" src="https://github.com/user-attachments/assets/6dfb45c4-2a8c-47c9-875a-48a938eddd20" />
<center>Grafo não direcionado demonstra a relação do Grupo 8 e suas principais empresas</center>
<br>
<center>Grafo do Grupo 7</center>
<img width="1532" height="813" alt="Grafo7" src="https://github.com/user-attachments/assets/3bec6a50-a2ef-4815-a658-a7540c68ff49" />
<center>Grafo não direcionado demonstra a relação do Grupo 7 e suas principais empresas</center>
<br>
<center>Grafo do Grupo 6</center>
<img width="1529" height="821" alt="Grafo6" src="https://github.com/user-attachments/assets/97655a7d-1e50-4120-a8ce-a82831dcf371" />
<center>Grafo não direcionado demonstra a relação do Grupo 6 e suas principais empresas</center>
<br>
<center>Grafo do Grupo 4</center>
<img width="1529" height="821" alt="Grafo5" src="https://github.com/user-attachments/assets/fee26b5f-598c-4a58-8a61-75895578f98b" />
<center>Grafo direcionado demonstra a relação do Grupo 4 e um problema de ciclo</center>

## Instalação 
**Linguagem**: Python, HTML, CSS e JavaScript<br>
**Framework**: Flask<br>
**Pré-requisitos**: Navegador instalado, Python, Flask , Flask_cors e Pandas presentes no computador e clonar o repositório localmente

## Passo a Passo
### 1. Clonar repositório:
```bash
https://github.com/projeto-de-algoritmos-2025/Grafos1_Grupos-Economicos.git
```
### 2. Instale as Dependências:
Abra um terminal ou prompt de comando na pasta do projeto e execute:
```bash
pip install Flask Flask-CORS pandas
```
### 3. Inicie o Servidor:
Digite no mesmo terminal:
```bash
python app.py
```
### 4. Acesse a Aplicação:
Abra seu navegador web e acesse o seguinte endereço: http://127.0.0.1:5001

## Uso

Selecione um grupo para visualizar o grafo e suas respectivas características.

## Outros 
Para adicionar um novo grupo de empresas ao projeto, é necessário atualizar os arquivos de dados que servem como a fonte de informação para a análise. Primeiro deve-se cadastrar as novas empresas como entidades individuais e, em seguida, especificar as relações de parceria ou controle que as conectam, formando assim um novo grupo que o sistema poderá reconhecer, analisar e exibir na interface.




