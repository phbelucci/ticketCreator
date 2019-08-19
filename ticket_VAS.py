from datetime import datetime
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('snelnxm83', '1525', service_name='BSCSIXFQA1') #if needed, place an 'r' before any parameter in order to address any special character such as '\'.
conn = cx_Oracle.connect(user=r'SYSADM', password='IX1bscs$.', dsn=dsn_tns) #if needed, place an 'r' before any parameter in order to address any special character such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()
resultado = c.execute("select * from CUSTOMER_ALL where CUSTCODE like '8.10001023%'")
for row in c:
    print(row)
conn.close()


# c = conn.cursor()
# resultado = c.execute("select * from CUSTOMER_ALL where CUSTCODE like '8.10001063%'")
# for row in c:
#     print(row)
# conn.close()


# Set Date to fill the ticket´s name
dataAtual = datetime.now()
dataAtualComHora = dataAtual.strftime('%y%m%d%H%M')
dataAtualString = str(dataAtualComHora)

# String Parameters to fill the ticket
callType = "2"
ticketData = input("Data e hora do bilhete no formato YYYYMM: ")
ticketDay = input("Dia: ")
ticketHour = str(ticketData[8:9])
ticketMinute = str(ticketData[10:11])
ticketSeconds = str(ticketData[12:13])
ticketOption = int(input("Digite o tipo do bilheter:\n1 - ORIGINADA 2 - RECEBIDA\n"))
while (ticketOption != 1)&(ticketOption!=2):
    print("Opção escolhida não é válida!")
    ticketOption = int(input("Digite o tipo do bilheter:\n1 - ORIGINADA 2 - RECEBIDA\n"))

if (ticketOption == 1):
    ticketType = "T29"
elif (ticketOption == 2):
    ticketType = "T30"


ticketMsisdn = input("Digite o MSISDN desejado: ")
ticketImsi = input("Informe o IMSI desejado: ")
ticketCGI = str(ticketImsi[0:7])
ticketRegion = str(ticketMsisdn[0:2])
ticketCentral = "551189848200"
ticketCentralCod = "STKM01"
ticketFinal = "1;1;41|"
qtdTickets = int(input("Quantidade de tickets: "))
cabecalhoArquivo = "INFO01-23551-"
finalArquivo = "-IF.TTF"
nomeArquivo = cabecalhoArquivo+dataAtualString+finalArquivo

def incrementaTempo(seconds,minutes,hours,day):
    ticketSeconds = seconds
    ticketMinute = minutes
    ticketHour = hours
    ticketDay = day

    newSecond = int(ticketSeconds) + 1
    if newSecond == 60:
        newSecond = 00
        ticketSeconds = "0" + str(newSecond)
        newMinute = int(ticketMinute) + 1
        if newMinute == 60:
            newMinute = 00
            ticketMinute = "0" + str(newMinute)
            newHour = int(ticketHour) + 1
            if newHour < 10:
                ticketHour = "0" + str(newHour)
            else:
                ticketHour = str(newHour)
                if newHour == 24:
                    newHour = 00
                    ticketHour = "0" + str(newHour)
                    newDay = int(ticketDay) + 1
                    ticketDay = str(newDay)
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
    return ticketSeconds,ticketMinute,ticketHour


# Open and create the file that will be edited
with open("C:\\Users\\PauloBelucciBelucci\\Desktop\\INFOTIM-TESTES-CENARIOS\BILHETES\\PythonAuto\\"+nomeArquivo,"w") as newTicket:

    # Executa o looping conforme a quantidade de bilhete desejada
    for ticket in range(qtdTickets):

        # cria o componente com tipo de envio T21
        createContent21 = newTicket.write(callType+";"+ticketData+ticketDay+ticketHour+ticketMinute+ticketSeconds+";"
                                          +ticketType+";"+ticketMsisdn+";"+ticketImsi+";"+ticketCGI+";"
                                          +ticketRegion+";"+ticketCentral+";"+ticketCentralCod+";"
                                          +ticketFinal+"\n")

        # Incrementa o horário da emissão do bilhete
        incrementaTempo(ticketSeconds,ticketMinute,ticketHour,ticketDay)
        resultado = incrementaTempo(ticketSeconds,ticketMinute,ticketHour,ticketDay)
        ticketSeconds = resultado[0]
        ticketMinute = resultado[1]
        ticketHour = resultado[2]
        ticketDay = resultado[3]

# mensagem de sucesso da emissão dos bilhetes
print(f"\n{qtdTickets} foram emitidos com sucesso. O nome do arquivo é {nomeArquivo}.")