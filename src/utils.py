import os

def ler_arquivo_entrada(caminho):
    if not os.path.exists(caminho):
        print(f"Erro: {caminho} não existe.")
        return []

    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    # Split manual por bloco (duas quebras de linha)
    blocos_brutos = conteudo.split('\n\n')
    textos = []
    for b in blocos_brutos:
        limpo = b.strip()
        if len(limpo) > 0:
            textos.append(limpo)
            
    return textos

def formatar_saida(indice, texto_original, mapa_codigos, texto_comprimido, frequencias):
    linhas = []
    linhas.append(f"=== TEXTO {indice} ===")
    
    # Recorte manual da string para preview
    preview = texto_original
    if len(preview) > 100:
        preview = preview[0:100] + "..."
    linhas.append(f"Original: {preview}")
    
    linhas.append("\n--- Tabela (Ordenada por Tamanho do Código) ---")
    linhas.append(f"{'TOKEN'.ljust(15)} | {'FREQ'.ljust(5)} | {'CÓDIGO'}")
    linhas.append("-" * 45)
    
    # --- MUDANÇA AQUI: Usando o sort nativo do Python ---
    # Convertemos o dicionário em lista de tuplas: [('token', '01'), ...]
    # key=lambda x: len(x[1]) -> Ordena pelo tamanho da string do código (2º item da tupla)
    lista_ordenada = sorted(mapa_codigos.items(), key=lambda x: len(x[1]))

    for palavra, codigo in lista_ordenada:
        # Recupera a frequência original (usando a palavra minúscula se necessário)
        # O .get previne erro caso a chave tenha mudado de caixa
        freq = frequencias.get(palavra, 0)
        
        linhas.append(f"{palavra.ljust(15)} | {str(freq).ljust(5)} | {codigo}")
        
    linhas.append("\n--- Texto Comprimido ---")
    linhas.append(texto_comprimido)
    linhas.append("\n" + "="*45 + "\n")
    
    return "\n".join(linhas)

def salvar_arquivo_saida(caminho, conteudo):
    try:
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"Salvo em: {caminho}")
    except Exception as e:
        print(f"Erro no disco: {e}")