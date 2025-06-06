print("Seja muito bem-vindo ao quiz!")

while True:
    resposta = input("\nGostaria de iniciar a sessão? (sim/não): ").strip().lower()

    if resposta == "sim":
        print("Começando...")

        pontuação = 0

        print("\nQ1.Qual das alternativas é um sistema operacional?")
        print("a) Python\nb) Windows\nc) Google\nd) HTML")
        resposta1 = input ("Resposta: ").strip().lower()
        if resposta1 == "b":
            pontuação += 1
        
        print("\nQ2.O que significa 'backup'?")
        print("a) Apagar arquivos antigos\nb) Atualizar o sistema\nc) Cópia de segurança dos dados\nd) Instalar programas novos")
        resposta2 = input ("Resposta: ").strip().lower()
        if resposta2 == "c":
            pontuação += 1
        
        print("\nQ3.Qual das opções representa um dispositivo de armazenamento?")
        print("a) Monitor\nb) Mouse\nc) Pendrive\nd) Teclado")
        resposta3 = input ("Resposta: ").strip().lower()
        if resposta3 == "c":
            pontuação += 1

        print("\nQ4.Um firewall serve para:")
        print("a) Controlar o tráfego de rede e bloquear acessos indevidos\nb) Proteger contra vírus\nc) Criar senhas fortes\nd) Otimizar a internet")
        resposta4 = input ("Resposta: ").strip().lower()
        if resposta4 == "a":
            pontuação += 1

        print("\nQ5.Qual linguagem é mais usada para criar sites?")
        print("a) C++\nb) Excel\nc) Python\nd) HTML")
        resposta5 = input ("Resposta: ").strip().lower()
        if resposta5 == "d":
            pontuação += 1

        print("\nQuiz finalizado com sucesso, parabéns!")
        print(f"Sua pontuação é {pontuação} de 5.")

        print("\nObrigada por realizar o quiz!")
        break

    elif resposta == "não":
        print("Voltando... Que tal tentar novamente?")
        break

    else:
        print("Resposta inválida! Por favor, opte por digitar 'sim' ou 'não'.")
        