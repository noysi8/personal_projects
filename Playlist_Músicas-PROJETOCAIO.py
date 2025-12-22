playlist = []
tela_inicial = """=== Playlist ===
1 - Adicionar música
2 - Listar músicas
3 - Remover música
4 - Buscar música
5 - Sair
6 - MODO ARQUIVOS TXT
"""
while True:
    print(tela_inicial)
    escolha = int(input("Escolha: "))
    if escolha == 1:
        musica = input("Nome da música: ")
        artista = input("Nome do artista: ")
        playlist.append([musica,artista])
        print(f"Musica '{musica}' adicionada com sucesso!")
    elif escolha == 2:
        indice = 0
        while indice < len(playlist):
            print(f"Nome da música: {playlist[indice][0]} (Artista: {playlist[indice][1]})")
            indice = indice + 1
    elif escolha == 3:
        indice = 0
        while indice < len(playlist):
            print(f"Música:{playlist[indice][0]} Indíce:{indice}")
            indice = indice + 1
        remover = int(input("Digite o ÍNDICE da música que deseja remover: "))
        if remover < len(playlist):
            removida = playlist.pop(remover)
            print(f"Música '{removida[0]}' removida com sucesso!")
        else:
            print("Índice errado!")
    elif escolha == 4:
        busca = input("Digite o nome da música para buscar: ")
        busca = busca.lower()
        indice = 0
        resultados = 0
        while indice < len(playlist):
            song = playlist[indice][0]
            if busca in song.lower():
                print(f"Nome da música: {song} (Artista: {playlist[indice][1]})")
                resultados += 1
            indice = indice + 1
        if resultados == 0:
            print("A música não foi encontrada!")
    elif escolha == 5:
        print("Saindo...")
        break
    elif escolha == 6:
        from pathlib import Path
        PASTA_PLAYLISTS = Path("playlists")
        PASTA_PLAYLISTS.mkdir(exist_ok=True)
        arquivos = list(PASTA_PLAYLISTS.iterdir())
        print("\n---ARQUIVOS DISPONÍVEIS---")
        for indice, arquivo in enumerate(arquivos):
            print(f"{indice} - {arquivo.name}")
        ler_salvar = input("Digite 'L' para ler ou 'S' para salvar(0 para sair):")
        if ler_salvar.lower() == "s":
            nome_arquivo = input("Digite o nome do arquivo: ")
            endereço_completo = PASTA_PLAYLISTS / f"{nome_arquivo}.txt"
            with open(endereço_completo, "w", encoding="utf-8") as arquivo:
                for item in playlist:
                    arquivo.write(f"Música: {item[0]} | Artista: {item[1]}\n")
            print(f"Playlist salva em: {endereço_completo}")
        elif ler_salvar.lower() == "l":
            numero_arquivo = int(input("Digite o índice do arquivo que deseja ler: "))
            if 0 <= numero_arquivo < len(arquivos):
                endereço_completo = arquivos[numero_arquivo]
                with open(endereço_completo, "r", encoding="utf-8") as arquivo:
                    print(f"\n---Conteúdo do arquivo {endereço_completo.name}---")
                    conteudo = arquivo.read()
                    print(conteudo)
            else:
                print("Índice inválido!")
        elif ler_salvar == "0":
            continue