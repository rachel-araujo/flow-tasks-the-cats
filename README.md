# Resumo do Projeto: Consumindo a API TheCatAPI com Prefect

## Descrição
Neste projeto, utilizei a biblioteca Prefect para criar um fluxo (flow) que consome dados de uma API externa, especificamente a TheCatAPI. 
O objetivo é construir tarefas (flow tasks) que interajam com pelo menos dois endpoints relacionados da API, simulando um timeout em um deles 
e utilizando a funcionalidade de retry para continuar o fluxo mesmo em caso de falhas temporárias.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal do projeto.
- **Prefect**: Biblioteca utilizada para orquestrar o fluxo de trabalho.
- **Requests**: Biblioteca utilizada para realizar requisições HTTP.

## Funcionalidades Implementadas
1. **Fetch Random Cat Image**: Uma tarefa que obtém uma imagem aleatória de um gato a partir da TheCatAPI.
2. **Fetch Random Cat Fact**: Uma tarefa que obtém um fato aleatório sobre gatos a partir da API Catfact.ninja.
3. **Display Results**: Uma tarefa que imprime a URL da imagem do gato e o fato sobre gatos no console e abre a imagem no navegador.

## Fluxo do Projeto
1. **Criar e configurar o ambiente**: Configurar o ambiente de desenvolvimento com as bibliotecas necessárias (Prefect e Requests).
2. **Definir as tarefas**:
    - **Fetch Random Cat Image**: Realiza uma requisição ao endpoint de imagens da TheCatAPI e retorna a URL da imagem.
    - **Fetch Random Cat Fact**: Realiza uma requisição ao endpoint de fatos da API Catfact.ninja e retorna um fato aleatório sobre gatos.
    - **Display Results**: Recebe a URL da imagem e o fato e os imprime no console, além de abrir a imagem no navegador.
3. **Configurar retry e timeout**: Configurar retries nas tarefas para lidar com falhas temporárias.
4. **Executar o fluxo**: Orquestrar as tarefas utilizando um fluxo do Prefect.