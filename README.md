# Reações

**Número da Lista**: 7

**Conteúdo da Disciplina**: Grafos 2

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0099353  |  Cibele Freitas Goudinho |
| 16/0127327  |  João Paulo Coelho de Souza |

## Sobre 
Nesse projeto visamos aplicar os conhecimentos de Grafos 2 trazendo para o contexto do jogo Assassin's Creed Odyssey. Nossa aplicação gera um grafo com peso nas arestas com base no mapa do jogo, onde as cidades são os nós e as arestas são a distância mais o nível necessário para cada cidade (os pesos estão definidos na imagem 1). O objetivo do projeto é ajudar os jogadores à achar a melhor rota para que ele chegue em uma cidade destino de sua escolha considerando seu nível e a distância em jogo de uma cidade para outra.
A distância foi calculada da seguinte forma:
DT = D + LV
Onde D é a distância entre as cidades, variando de 1-9
E LV é: MinL - MaxL
Na qual MinL é o menor nível da cidade e o MaxL o maior nível da cidade, por exemplo Achaia (42-46) o MinL seria 42 e o MaxL seria 46. 
No cálculo é considerado o MinL da cidade com maiores níveis e o MaxL da cidade com menores níveis, ao exemplo de: Achaia e Kephallonia o MinL seria de Achaia(42) e o MaxL de Kephallonia(6), assim LV = 42 - 6 = 36 e D = 3 e DT = 3 + 36 = 39

## Screenshots
### Caminhos entre as cidades
![Mapa com pesos para base](assets/mapDistances.png)
### Mapa Original
![Mapa do jogo](assets/map.png)
### Grafo
![Grafo](assets/graph.png)
### Tela Inicial
![Tela Inicial](assets/homePage.png)
### Resultado da Busca
![Resultado da Busca](assets/resultPage.png)

## Instalação 
**Linguagem**: Python e ReactJS<br>
**Framework**: FastAPI<br>
Precisa rodar o front e o back ao mesmo tempo, recomenda-se utilizar dois terminais para tal, um na pasta back e outra na pasta front.
### Dentro da pasta back: 
Pode ser que utilize python ao invés de python3 (válido para todos os comandos)
Entrar no back:
```
cd back
```
Criar env:
```
python3 -m venv .venv
```
Ativar env:
```
source .venv/bin/activate
```
Instalar requirements:
```
pip install -r requirements.txt
```
Rodar o projeto:
```
uvicorn main:app --reload 
```
Se quiser ver o grafo gerado executar e verificar o arquivo graph.png:
```
python3 CitiesGraph.py
```
Caso o seguinte erro se apresente:
```
qt.qpa.plugin: Could not find the Qt platform plugin "1" in ""
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
```
Rodar o comando no console: 
```
export QT_QPA_PLATFORM=offscreen
```
Em seguida rodar novamente o arquivo:
```
python3 CitiesGraph.py
```
### Dentro da pasta front:
Entrar no front:
```
cd front
```
```
npm install
```
```
npm start
```
## Uso 
1. Escolha seu nível correspondente ao seu nível no jogo Assassin's Creed Odyssey (válido de 1 a 19) 
2. No primeiro dropdown escolher qual das cidades quer começar com base no nível escolhido 
3. No segundo dropdown escolher qual seria a cidade destino desejada
4. Clicar em enviar
5. Se quiser fazer uma nova consulta clicar em refazer 

## Outros 
Projeto baseado no jogo [Assassin's Creed Odyssey](https://www.ubisoft.com/pt-br/game/assassins-creed/odyssey).





