import webbrowser

def abrir_links():
    print("Digite os links, um por linha. Para finalizar, deixe uma linha em branco e pressione Enter.")
    links = []
    while True:
        link = input()
        if not link:  # Se a entrada estiver em branco, pare de pedir mais links
            break
        # Verifica se o link começa com "http://" ou "https://", se não começar, adiciona "http://"
        if not link.startswith("http://") and not link.startswith("https://"):
            link = "http://" + link
        links.append(link)

    for link in links:
        webbrowser.open(link)

abrir_links()
