import mysql.connector
from PyQt5 import uic, QtWidgets
from reportlab.pdfgen import canvas

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_pibex"
)

def gerar_pdf():
    try:
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM cadastro"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        #print(dados_lidos)
        y = 0
        pdf = canvas.Canvas("cadastro_pibex.pdf")
        pdf.setFont("Times-Bold", 6)
        pdf.drawString(200, 800, "Bolsistas cadastrados:")
        pdf.setFont("Times-Bold", 4)

        pdf.drawString(6, 750, "ID")
        pdf.drawString(66, 750, "PROCESSO DE INDICAÇÃO")
        pdf.drawString(126, 750, "DATA DE VÍNCULO")
        pdf.drawString(186, 750, "SITUAÇÃO DO BOLSISTA")
        pdf.drawString(246, 750, "PROCESSO DE DESLIGAMENTO")
        pdf.drawString(306, 750, "DATA DE DESLIGAMENTO")
        pdf.drawString(366, 750, "PROCESSOS ALTERAÇÃO DE ORIENTAÇÃO")
        pdf.drawString(426, 750, "SITUACAO DA ORIENTAÇÃO")
        pdf.drawString(486, 750, "DATA-ÍNICIO")
        pdf.drawString(546, 750, "DATA-FIM")
        pdf.drawString(606, 750, "PROJETO")
        pdf.drawString(666, 750, "CÓDIGO")
        pdf.drawString(726, 750, "LOTAÇÃO")

        for i in range(0, len(dados_lidos)):
            y += 10
            pdf.drawString(6, 750 - y, str(dados_lidos[i][0]))
            pdf.drawString(66, 750 - y, str(dados_lidos[i][1]))
            pdf.drawString(126, 750 - y, str(dados_lidos[i][2]))
            pdf.drawString(186, 750 - y, str(dados_lidos[i][3]))
            pdf.drawString(246, 750 - y, str(dados_lidos[i][4]))
            pdf.drawString(306, 750 - y, str(dados_lidos[i][5]))
            pdf.drawString(366, 750 - y, str(dados_lidos[i][6]))
            pdf.drawString(426, 750 - y, str(dados_lidos[i][7]))
            pdf.drawString(486, 750 - y, str(dados_lidos[i][8]))
            pdf.drawString(546, 750 - y, str(dados_lidos[i][9]))
            pdf.drawString(606, 750 - y, str(dados_lidos[i][10]))
            pdf.drawString(666, 750 - y, str(dados_lidos[i][11]))
            pdf.drawString(726, 750 - y, str(dados_lidos[i][12]))


            pdf.save()
            print("PDF FOI GERADO COM SUCESSO!")

    except:
        print("não foi possivel criar o pdf")

# pegando os valores de cadastro
def funcao_principal():
    try:
        linha1 = formulario.lineEdit.text()
        linha2 = formulario.lineEdit_2.text()
        linha3 = formulario.lineEdit_3.text()
        linha4 = formulario.lineEdit_4.text()
        linha5 = formulario.lineEdit_5.text()
        linha6 = formulario.lineEdit_6.text()
        linha7 = formulario.lineEdit_7.text()
        linha8 = formulario.lineEdit_8.text()
        linha9 = formulario.lineEdit_9.text()
        linha10 = formulario.lineEdit_10.text()
        linha11 = formulario.lineEdit_11.text()
        linha12 = formulario.lineEdit_12.text()
        linha13 = formulario.lineEdit_13.text()
        linha14 = formulario.lineEdit_14.text()
        linha15 = formulario.lineEdit_15.text()
        linha16 = formulario.lineEdit_16.text()
        linha17 = formulario.lineEdit_17.text()
        linha18 = formulario.lineEdit_18.text()
        linha19 = formulario.lineEdit_19.text()
        linha20 = formulario.lineEdit_20.text()
        linha21 = formulario.lineEdit_21.text()
        linha22 = formulario.lineEdit_22.text()
        linha23 = formulario.lineEdit_23.text()
        linha24 = formulario.lineEdit_24.text()
        linha25 = formulario.lineEdit_25.text()
        linha26 = formulario.lineEdit_26.text()


        print("Dados", linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9, linha10, linha11, linha12,
              linha13, linha14, linha15, linha16, linha17, linha18,linha19,linha21,linha22,linha23,linha24,linha25,linha26)


        cursor = banco.cursor()
        comando_SQL = "INSERT INTO cadastro (PROCESSO_DE_INDICACAO,DATA_DE_VINCULO,SITUACAO_DO_BOLSISTA," \
                      "PROCESSO_DE_DESLIGAMENTO,DATA_DE_DESLIGAMENTO,PROCESSOS_ALTERACAO_DE_ORIENTACAO," \
                      "SITUACAO_DA_ORIENTACAO,DATA_INICIO,DATA_FIM,PROJETO,CODIGO,LOTACAO,E_MAIL_DO_A_ORIENTADOR_A," \
                      "E_MAIL_DO_A_BOLSISTA,ORIENTADOR_A,BOLSISTA,MATRICULA,CPF,BANCO,CODIGO_DO_BANCO,AGENCIA,OP," \
                      "CONTA_CORRENTE,VALOR,EDITAL,TIPO_DE_BOLSA) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                      "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        dados = (
        str(linha1), str(linha2), str(linha3), str(linha4), str(linha5), str(linha6), str(linha7), str(linha8), str(linha9),
        str(linha10), str(linha11), str(linha12), str(linha13), str(linha14), str(linha15), str(linha16), str(linha17),
        str(linha18),str(linha19),str(linha20),str(linha21),str(linha22),str(linha23),str(linha24),str(linha25),str(linha26))
        cursor.execute(comando_SQL, dados)
        banco.commit()
        formulario.lineEdit.setText("")
        formulario.lineEdit_2.setText("")
        formulario.lineEdit_3.setText("")
        formulario.lineEdit_4.setText("")
        formulario.lineEdit_5.setText("")
        formulario.lineEdit_6.setText("")
        formulario.lineEdit_7.setText("")
        formulario.lineEdit_8.setText("")
        formulario.lineEdit_9.setText("")
        formulario.lineEdit_10.setText("")
        formulario.lineEdit_11.setText("")
        formulario.lineEdit_12.setText("")
        formulario.lineEdit_13.setText("")
        formulario.lineEdit_14.setText("")
        formulario.lineEdit_15.setText("")
        formulario.lineEdit_16.setText("")
        formulario.lineEdit_17.setText("")
        formulario.lineEdit_18.setText("")
        formulario.lineEdit_19.setText("")
        formulario.lineEdit_20.setText("")
        formulario.lineEdit_21.setText("")
        formulario.lineEdit_22.setText("")
        formulario.lineEdit_23.setText("")
        formulario.lineEdit_24.setText("")
        formulario.lineEdit_25.setText("")
        formulario.lineEdit_26.setText("")
    except:
        print('Erro ao conectar com o banco de dados.')
    finally:
        cursor.close()

def chama_listagem():
    listar_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM cadastro"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_tela.tableWidget.setRowCount(len(dados_lidos))
    listar_tela.tableWidget.setColumnCount(27)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 27):
            listar_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def excluir_dados():
    linha = listar_tela.tableWidget.currentRow()
    listar_tela.tableWidget.removeRow(linha)


    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM cadastro WHERE id="+ str(valor_id))

def editar_dados():
    global numero_id

    linha = listar_tela.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM cadastro WHERE id=" + str(valor_id))
    dados = cursor.fetchall()
    tela_editar.show()

    numero_id = valor_id

    tela_editar.lineEdit.setText(str(dados[0][1]))
    tela_editar.lineEdit_2.setText(str(dados[0][2]))
    tela_editar.lineEdit_3.setText(str(dados[0][3]))
    tela_editar.lineEdit_4.setText(str(dados[0][4]))
    tela_editar.lineEdit_5.setText(str(dados[0][5]))
    tela_editar.lineEdit_6.setText(str(dados[0][6]))
    tela_editar.lineEdit_7.setText(str(dados[0][7]))
    tela_editar.lineEdit_8.setText(str(dados[0][8]))
    tela_editar.lineEdit_9.setText(str(dados[0][9]))
    tela_editar.lineEdit_10.setText(str(dados[0][10]))
    tela_editar.lineEdit_11.setText(str(dados[0][11]))
    tela_editar.lineEdit_12.setText(str(dados[0][12]))
    tela_editar.lineEdit_13.setText(str(dados[0][13]))
    tela_editar.lineEdit_14.setText(str(dados[0][14]))
    tela_editar.lineEdit_15.setText(str(dados[0][15]))
    tela_editar.lineEdit_16.setText(str(dados[0][16]))
    tela_editar.lineEdit_17.setText(str(dados[0][17]))
    tela_editar.lineEdit_18.setText(str(dados[0][18]))
    tela_editar.lineEdit_19.setText(str(dados[0][19]))
    tela_editar.lineEdit_20.setText(str(dados[0][20]))
    tela_editar.lineEdit_21.setText(str(dados[0][21]))
    tela_editar.lineEdit_22.setText(str(dados[0][22]))
    tela_editar.lineEdit_23.setText(str(dados[0][23]))
    tela_editar.lineEdit_24.setText(str(dados[0][24]))
    tela_editar.lineEdit_25.setText(str(dados[0][25]))
    tela_editar.lineEdit_26.setText(str(dados[0][26]))

def salvar_dados_editados():
    #numero do id
    global numero_id
    #valor digitado no lineEdit
    linha1 = tela_editar.lineEdit.text()
    linha2 = tela_editar.lineEdit_2.text()
    linha3 = tela_editar.lineEdit_3.text()
    linha4 = tela_editar.lineEdit_4.text()
    linha5 = tela_editar.lineEdit_5.text()
    linha6 = tela_editar.lineEdit_6.text()
    linha7 = tela_editar.lineEdit_7.text()
    linha8 = tela_editar.lineEdit_8.text()
    linha9 = tela_editar.lineEdit_9.text()
    linha10 = tela_editar.lineEdit_10.text()
    linha11 = tela_editar.lineEdit_11.text()
    linha12 = tela_editar.lineEdit_12.text()
    linha13 = tela_editar.lineEdit_13.text()
    linha14 = tela_editar.lineEdit_14.text()
    linha15 = tela_editar.lineEdit_15.text()
    linha16 = tela_editar.lineEdit_16.text()
    linha17 = tela_editar.lineEdit_17.text()
    linha18 = tela_editar.lineEdit_18.text()
    linha19 = tela_editar.lineEdit_19.text()
    linha20 = tela_editar.lineEdit_20.text()
    linha21 = tela_editar.lineEdit_21.text()
    linha22 = tela_editar.lineEdit_22.text()
    linha23 = tela_editar.lineEdit_23.text()
    linha24 = tela_editar.lineEdit_24.text()
    linha25 = tela_editar.lineEdit_25.text()
    linha26 = tela_editar.lineEdit_26.text()
    #atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE cadastro SET PROCESSO_DE_INDICACAO = '{}', DATA_DE_VINCULO = '{}', SITUACAO_DO_BOLSISTA = "
                   "'{}', PROCESSO_DE_DESLIGAMENTO = '{}', DATA_DE_DESLIGAMENTO = '{}', "
                   "PROCESSOS_ALTERACAO_DE_ORIENTACAO = '{}', SITUACAO_DA_ORIENTACAO = '{}', DATA_INICIO = '{}', "
                   "DATA_FIM = '{}', PROJETO = '{}', CODIGO = '{}',LOTACAO = '{}', E_MAIL_DO_A_ORIENTADOR_A = '{}', "
                   "E_MAIL_DO_A_BOLSISTA = '{}', ORIENTADOR_A = '{}', BOLSISTA = '{}', MATRICULA = '{}', CPF = '{}', "
                   "BANCO = '{}', CODIGO_DO_BANCO = '{}', AGENCIA = '{}', OP = '{}', CONTA_CORRENTE = '{}', "
                   "VALOR = '{}', EDITAL = '{}', TIPO_DE_BOLSA = '{}' WHERE id = {}".format(linha1,linha2,linha3,
                                                                                            linha4,linha5,linha6,
                                                                                            linha7,linha8,
                                                                                            linha9,linha10,linha11,
                                                                                            linha12,linha13,linha14,
                                                                                            linha15,linha16,linha17,
                                                                                            linha18,linha19,linha20,
                                                                                            linha21,linha22,linha23,
                                                                                            linha24,linha25,linha26,
                                                                                            numero_id))
    banco.commit()
    #atualizar as janelas
    tela_editar.close()
    listar_tela.close()
    chama_listagem()


app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
listar_tela = uic.loadUi("listagem.ui")
tela_editar = uic.loadUi("menuEditar.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_listagem)
listar_tela.pushButton.clicked.connect(gerar_pdf)
listar_tela.pushButton_2.clicked.connect(excluir_dados)
listar_tela.pushButton_3.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_dados_editados)

formulario.show()
app.exec()


