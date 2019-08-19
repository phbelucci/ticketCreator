from datetime import datetime
import os.path


# Set Date to fill the ticket´s name
dataAtual = datetime.now()
dataAtualComHora = dataAtual.strftime('%y%m%d%H%M')
dataAtualString = str(dataAtualComHora)

# String Parameters to fill the ticket
callType = "2"
ticketData = input("Data e hora do bilhete no formato YYYYMM: ")
while(len(ticketData) != 6):
    print("Valor incorreto, favor digitar novamente: ")
    ticketData = input("Data e hora do bilhete no formato YYYYMM: ")
ticketDay = input("Dia: ")
while(len(ticketDay) != 2):
    print("Valor incorreto, favor digitar novamente: ")
    ticketDay = input("Dia: ")

ticketHour = input("Hora: ")
ticketMinute = input("Minuto: ")
ticketSeconds = input("Segundo: ")
ticketType21 = "T21"
ticketType25 = "T25"
ticketMsisdn = "21982135456"
ticketImsi = "724022200962927"
ticketCGI = "7240221"
ticketRegion = "21"
ticketCentral = "551189848200"
ticketCentralCod = "STKM01"
ticketLA = input("Entre com a LA: ")
ticketFinal = "1;1;41|"
qtdTickets = int(input("Quantidade de tickets: "))
cabecalhoArquivo = "INFO01-23551-"
finalArquivo = "-IF.TTF"
nomeArquivo = cabecalhoArquivo+dataAtualString

def incrementaTempo(seconds,minutes,hours,dia):
    ticketSeconds = seconds
    ticketMinute = minutes
    ticketHour = hours
    ticketDay = dia

    newSecond = int(ticketSeconds) + 1
    if newSecond == 60:
        newSecond = 00
        ticketSeconds = "0" + str(newSecond)

        newMinute = int(ticketMinute) + 1
        if newMinute == 60:
            newMinute = 00
            ticketMinute = "0" + str(newMinute)

            newHour = int(ticketHour) + 1
            if newHour == 24:
                newHour = 00
                ticketHour = "0" + str(newHour)
                newDay = int(ticketDay) + 1
                ticketDay = str(newDay)

            if newHour < 10:
                ticketHour = "0" + str(newHour)
            else:
                ticketHour = str(newHour)
        else:
            if newMinute < 10:
                ticketMinute = "0" + str(newMinute)
            else:
                ticketMinute = str(newMinute)
    else:
        if newSecond < 10:
            ticketSeconds = "0" + str(newSecond)
        else:
            ticketSeconds = str(newSecond)

    return ticketSeconds,ticketMinute,ticketHour,ticketDay



# Open and create the file that will be edited
with open("C:\\Users\\PauloBelucciBelucci\\Desktop\\INFOTIM-TESTES-CENARIOS\\BILHETES\\PythonAuto\\"+nomeArquivo+finalArquivo,"w") as newTicket:

    # Executa o looping conforme a quantidade de bilhete desejada
    for ticket in range(qtdTickets):

        # cria o componente com tipo de envio T21
        createContent21 = newTicket.write(callType+";"+ticketData+ticketDay+ticketHour+ticketMinute+ticketSeconds+";"
                                          +ticketType21+";"+ticketMsisdn+";"+ticketImsi+";"+ticketCGI+";"
                                          +ticketRegion+";"+ticketCentral+";"+ticketCentralCod+";"+ticketLA+";"
                                          +ticketFinal+"\n")

        # Incrementa o horário da emissão do bilhete
        incrementaTempo(ticketSeconds,ticketMinute,ticketHour,ticketDay)
        resultado = incrementaTempo(ticketSeconds,ticketMinute,ticketHour,ticketDay)
        ticketSeconds = resultado[0]
        ticketMinute = resultado[1]
        ticketHour = resultado[2]
        ticketDay = resultado[3]

        # cria o componente com tipo de envio T25
        createContent25 = newTicket.write(callType + ";" + ticketData + ticketDay + ticketHour+ticketMinute+ticketSeconds+";"
                                          + ticketType25 + ";1" + ticketMsisdn + ";" + ticketImsi + ";" + ticketCGI +
                                          ";" + ticketRegion + ";" + ticketCentral + ";" + ticketCentralCod + ";" +
                                          ticketLA + ";" + ticketFinal + "\n")

        # Incrementa o horário da emissão do bilhete
        incrementaTempo(ticketSeconds,ticketMinute,ticketHour,ticketDay)
        resultado = incrementaTempo(ticketSeconds, ticketMinute, ticketHour,ticketDay)
        ticketSeconds = resultado[0]
        ticketMinute = resultado[1]
        ticketHour = resultado[2]
        ticketDay = resultado[3]

# mensagem de sucesso da emissão dos bilhetes
print(f"\n{qtdTickets} foram emitidos com sucesso, para o LA {ticketLA}. O nome do arquivo é {nomeArquivo+finalArquivo}.")