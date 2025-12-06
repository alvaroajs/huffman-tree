class No:
    def __init__(self, palavra, frequencia):
        self.palavra = palavra
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

def tokenizar_manualmente(texto):
    """
    Percorre a string caractere por caractere.
    Não usa regex nem split.
    """
    tokens = []
    buffer = ""
    
    # Define manualmente o que é separador
    # Se quiser ser BEM raiz, definimos string de pontuação
    pontuacoes = ".,!?:; "
    
    for i in range(len(texto)):
        char = texto[i]
        
        # Verifica se o char atual NÃO é pontuação/espaço
        eh_letra = True
        for p in pontuacoes:
            if char == p:
                eh_letra = False
                break
        
        if char == "\n": # Quebra de linha também é separador
            eh_letra = False

        if eh_letra:
            buffer += char
        else:
            # Se tinha palavra acumulada, salva
            if len(buffer) > 0:
                tokens.append(buffer)
                buffer = ""
            
            # Se for pontuação (não espaço), salva ela também
            if char != " " and char != "\n":
                tokens.append(char)
                
    # Salva o resto do buffer se sobrou
    if len(buffer) > 0:
        tokens.append(buffer)
        
    return tokens

def extrair_menor_no(lista_nos):
    """
    LÓGICA LOW LEVEL:
    Percorre a lista inteira para achar o índice do nó com menor frequência.
    Remove e retorna esse nó.
    Substitui o .sort() ou heapq.
    """
    if len(lista_nos) == 0:
        return None
        
    menor_indice = 0
    menor_freq = lista_nos[0].frequencia
    
    # Loop manual (Busca Linear)
    for i in range(1, len(lista_nos)):
        freq_atual = lista_nos[i].frequencia
        
        # Critério: Menor frequência. 
        # Desempate: Se igual, pega o que apareceu antes (estabilidade simples)
        if freq_atual < menor_freq:
            menor_freq = freq_atual
            menor_indice = i
            
    # Remove o nó da lista manualmente
    no_removido = lista_nos.pop(menor_indice)
    return no_removido

def construir_arvore(texto):
    # 1. Tokenização "na unha"
    tokens_originais = tokenizar_manualmente(texto)
    
    # 2. Contagem e Normalização Manual
    frequencias = {}
    tokens_normalizados = []
    
    for token in tokens_originais:
        # Lowercase manual (usando built-in do char, mas lógica explicita)
        token_low = token.lower()
        tokens_normalizados.append(token_low)
        
        if token_low in frequencias:
            frequencias[token_low] += 1
        else:
            frequencias[token_low] = 1
            
    if len(frequencias) == 0:
        return None, {}, []

    # 3. Transforma dict em lista de Nós
    lista_nos = []
    for chave in frequencias:
        valor = frequencias[chave]
        novo_no = No(chave, valor)
        lista_nos.append(novo_no)
    
    # 4. Algoritmo de Huffman Manual
    # Enquanto tiver mais de 1 nó, junta os dois menores
    while len(lista_nos) > 1:
        # Busca linear pelo 1º menor
        no1 = extrair_menor_no(lista_nos)
        
        # Busca linear pelo 2º menor (que sobrou na lista)
        no2 = extrair_menor_no(lista_nos)
        
        # Cria pai
        soma = no1.frequencia + no2.frequencia
        pai = No(None, soma)
        pai.esquerda = no1
        pai.direita = no2
        
        # Insere de volta no fim da lista
        lista_nos.append(pai)
        
    # O último que sobrar é a raiz
    raiz = lista_nos[0]
    return raiz, frequencias, tokens_normalizados

def gerar_mapa_codigos(no, codigo_atual="", mapa=None):
    if mapa is None:
        mapa = {}
    
    # É folha se tem palavra associada
    if no.palavra is not None:
        # Tratamento para caso de 1 única palavra no texto todo
        if codigo_atual == "":
            mapa[no.palavra] = "0"
        else:
            mapa[no.palavra] = codigo_atual
        return mapa

    if no.esquerda is not None:
        gerar_mapa_codigos(no.esquerda, codigo_atual + "0", mapa)
    
    if no.direita is not None:
        gerar_mapa_codigos(no.direita, codigo_atual + "1", mapa)
        
    return mapa

def comprimir_texto(tokens_normalizados, mapa_codigos):
    lista_codigos = []
    
    for token in tokens_normalizados:
        if token in mapa_codigos:
            codigo = mapa_codigos[token]
            lista_codigos.append(codigo)
        else:
            # Caso de erro (não deve ocorrer)
            print(f"ERRO: {token} não achado.")
            
    # Join é permitido pois é manipulação de string básica
    return " ".join(lista_codigos)