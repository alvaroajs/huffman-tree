import os
import huffman
import utils

CAMINHO_INPUT = os.path.join("../data", "input.dat")
CAMINHO_OUTPUT = os.path.join("../data", "output.dat")

def main():
    print("Iniciando Huffman (Low Level)...")
    
    textos = utils.ler_arquivo_entrada(CAMINHO_INPUT)
    if not textos:
        print("Sem dados em data/input.dat")
        return

    relatorio_final = ""

    for i, texto in enumerate(textos, start=1):
        print(f"Processando Texto {i}...")
        
        # Retorna a raiz, as frequencias e a lista de tokens já convertida para minúsculo
        raiz, frequencias, tokens_tratados = huffman.construir_arvore(texto)
        
        if raiz:
            mapa_codigos = huffman.gerar_mapa_codigos(raiz)
            
            # Passamos a lista de tokens já tratada, não o texto bruto
            texto_comprimido = huffman.comprimir_texto(tokens_tratados, mapa_codigos)
            
            relatorio = utils.formatar_saida(i, texto, mapa_codigos, texto_comprimido, frequencias)
            relatorio_final += relatorio
        else:
            print(f"Aviso: Texto {i} inválido.")

    utils.salvar_arquivo_saida(CAMINHO_OUTPUT, relatorio_final)

if __name__ == "__main__":
    main()