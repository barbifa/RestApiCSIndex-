#coding: utf8
from flask import Flask
from flask import make_response
import StringIO
import csv
from flask import request
import sys
import os

app = Flask(__name__, template_folder='templates')

#Número de publicações em uma determinada conferência de uma área
@app.route('/nPubConferenciasDeUmaArea/<string:conferencia>/<string:area>')
def nPubConferenciasDeUmaArea(conferencia, area):
    filename = "./data/"+ area + "-out-confs.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data :
            if(row[0] == conferencia):
                #return str(row[1])
                DATA.append(row)

    with open('Resultado_nPub_'+conferencia+'_'+area+'.csv', 'w') as csvfile:

        header = ['Conferencia da area ' + area, 'Quantidade de publicacoes']
        writer = csv.DictWriter(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames= header)
        writer.writeheader()

        for row in DATA:
            writer.writerow({'Conferencia da area ' + area: row[0], 'Quantidade de publicacoes': row[1]})

    return 'Arquivo salvo!'

#Scores de todos os departamentos em uma área
@app.route('/scoresDepartamentosDaArea/<string:area>')
def scoresDepartamentosDaArea(area):
    filename = "./data/"+ area + "-out-scores.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data :
            DATA.append(row)

    with open('scoresDepartamentos_'+area+'.csv', 'w') as csvfile:

        header = ['Departamento da area ' + area, 'Score']
        writer = csv.DictWriter(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames= header)
        writer.writeheader()

        for row in DATA:
            writer.writerow({'Departamento da area ' + area: row[0], 'Score': row[1]})

    return 'Arquivo salvo!'

#Número de professores que publicam em uma determinada área (organizados por departamentos)
@app.route('/nProfessoresArea/<string:area>')
def nProfessoresArea(area):
    filename = "./data/"+ area + "-out-profs.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data :
            DATA.append(row)

    with open('nProfessoresArea'+area+'.csv', 'w') as csvfile:

        header = ['Departamento da area ' + area, 'Numero de professores']
        writer = csv.DictWriter(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames= header)
        writer.writeheader()

        for row in DATA:
            writer.writerow({'Departamento da area ' + area: row[0], 'Numero de professores': row[1]})

    return 'Arquivo salvo!'

#Todos os papers de uma área (ano, título, deptos e autores)
@app.route('/papersArea/<string:area>')
def papersArea( area):
    filename = "./data/"+ area + "-out-papers.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data :
            DATA.append(row)

    with open('papers_'+area+'.csv', 'w') as csvfile:

        header = ['Ano', 'Titulo', 'Departamento', 'Autores']
        writer = csv.DictWriter(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames= header)
        writer.writeheader()

        for row in DATA:
            writer.writerow({'Ano': row[0], 'Titulo': row[2], 'Departamento':row[3], 'Autores':row[4]})

    return 'Arquivo salvo!'

#Todos os papers de um departamento em uma área
@app.route('/papersDepartamentoArea/<string:departamento>/<string:area>')
def papersDepartamentoArea(departamento, area):
    filename = "./data/"+ area + "-out-papers.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data :
            if(row[1] == departamento):
                DATA.append(row)

    with open('papers_'+departamento+'_'+area+'.csv', 'w') as csvfile:

        header = ['Departamento da area ' + area, 'Paper']
        writer = csv.DictWriter(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames= header)
        writer.writeheader()

        for row in DATA:
            writer.writerow({'Departamento da area ' + area: row[1], 'Paper': row[2]})

    return 'Arquivo salvo!'


if __name__ == '__main__':      
    app.run(debug=True)