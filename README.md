# Implementação do Código de Huffman

Este projeto apresenta uma implementação prática do algoritmo de Huffman para compressão de texto sem perdas. O trabalho foi desenvolvido como parte da avaliação da disciplina de Algoritmos e Estruturas de Dados.

**Autor:** Michel Pires
**Data:** 06/12/2025

## 📋 Sobre o Projeto

O software lê um conjunto de frases, calcula a frequência das palavras e constrói uma Árvore de Huffman binária para gerar códigos otimizados. Palavras mais frequentes recebem códigos binários menores, resultando na compressão dos dados.

### Diferenciais da Implementação
* **Lógica "Low Level":** A construção da árvore, filas de prioridade e tokenização foram implementadas manualmente, sem depender de bibliotecas prontas de complexidade (como `heapq` ou `Collections`).
* **Estrutura Modular:** Código organizado em módulos (`huffman`, `utils`, `main`) seguindo boas práticas.
* **Compatibilidade:** Desenvolvido em Python puro, compatível com Linux e Windows.

## 🚀 Como Executar

### Pré-requisitos
* Python 3.x instalado.

### Passo a Passo

1.  Clone o repositório:
    ```bash
    git clone <URL_DO_SEU_REPO>
    cd huffman-tree
    ```

2.  Execute o programa principal:
    ```bash
    python3 src/main.py
    ```

3.  Verifique os resultados:
    * A entrada de dados está em: `data/input.dat`
    * O relatório de compressão será gerado em: `data/output.dat`

## 📂 Estrutura de Arquivos

```text
/
├── src/
│   ├── main.py       # Ponto de entrada do programa
│   ├── huffman.py    # Lógica da Árvore, Nós e Compressão
│   └── utils.py      # Manipulação de arquivos e formatação
├── data/
│   ├── input.dat     # Textos originais para compressão
│   └── output.dat    # Relatório gerado com as árvores e binários
├── .gitignore        # Arquivos ignorados pelo Git
└── README.md         # Documentação do projeto
