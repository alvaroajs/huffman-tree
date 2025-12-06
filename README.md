# Implementação do Código de Huffman

Este projeto apresenta uma implementação prática do algoritmo de Huffman para compressão de texto sem perdas. O trabalho foi desenvolvido como parte da avaliação da disciplina de Algoritmos e Estruturas de Dados.


# 📖 Sobre o Projeto

Este trabalho foi desenvolvido com um objetivo principal: **entender na prática como funcionam os algoritmos de compressão**.

A ideia não é apenas "fazer o código rodar", mas sim explorar como estruturas de dados (especificamente Árvores Binárias e Filas de Prioridade) podem ser usadas para resolver problemas reais — neste caso, fazer um texto ocupar menos espaço no disco sem perder nenhuma informação.

O programa utiliza o **Algoritmo de Huffman**, que é a base de formatos famosos como ZIP e MP3. Ele analisa estatisticamente o texto: palavras que aparecem muito ganham códigos curtos (economizando bits), e palavras raras ficam com códigos mais longos.

## 🧠 Diferenciais da Implementação

Para garantir um aprendizado real ("Low Level"), este projeto **não utiliza bibliotecas prontas** do Python para as partes críticas (como `heapq` ou `Counter`). Toda a lógica foi construída manualmente:

* **Tokenização Inteligente (Pontuação):** O programa é capaz de entender a estrutura do texto. Ele não enxerga "Brasil," como uma palavra só. Ele separa o texto em `Brasil` e `,`. Isso garante que pontuações como vírgulas, pontos e exclamações sejam preservadas e comprimidas individualmente, permitindo uma reconstrução perfeita do original.
* **Construção Manual da Árvore:** A montagem dos nós e a varredura para criar os códigos binários (0 para esquerda, 1 para direita) foram feitas "na unha" para demonstrar domínio da lógica.
* **Ordenação e Busca:** Algoritmos de ordenação e busca linear foram implementados manualmente para gerenciar a fila de prioridade.

## 📂 Estrutura do Código

O projeto está organizado para ser fácil de ler e manter:

* `src/main.py`: O maestro. Gerencia a leitura dos arquivos e chama as funções.
* `src/huffman.py`: O cérebro. Contém a lógica pesada de criar a árvore, gerar os bits e separar as palavras das pontuações.
* `src/utils.py`: O assistente. Cuida da leitura do disco e deixa o relatório final bonito e legível.

## 🚀 Como Rodar

É bem simples ver o projeto funcionando:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/alvaroajs/huffman-tree/
    cd huffman-tree
    ```

2.  **Execute:**
    ```bash
    python3 src/main.py
    ```

3.  **Veja a mágica:**
    O programa vai ler o arquivo `data/input.dat` e gerar um relatório completo em `data/output.dat`.

## 📊 Exemplo de Resultado

No arquivo de saída, você verá como o algoritmo trata cada palavra e pontuação separadamente:

```text
=== TEXTO EXEMPLO ===
Original: Olá, mundo!

--- Tabela de Códigos ---
TOKEN           | FREQ  | CÓDIGO
--------------------------------
Olá             | 1     | 00
,               | 1     | 01    <-- Veja a vírgula separada aqui!
mundo           | 1     | 10
!               | 1     | 11


