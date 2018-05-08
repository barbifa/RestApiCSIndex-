from flask import Flask
from flask import make_response
import StringIO
import csv
import StringIO
from flask import request

app = Flask(__name__)

@app.route("/<int:question>")
def apiRestCSIndex(question):

	if question == 1:
		conferencia = request.args['conferencia']
		area = request.args["area"]
		return numeroDePublicacoesEmUmaDeterminadaConferenciaDeUmaArea(conferencia,area)
	elif question == 2:
		return "dasdasdasdasda";
		
	else:
		abort(404)	


def numeroDePublicacoesEmUmaDeterminadaConferenciaDeUmaArea(conferencia,area):

	
	data = [
	    ["REVIEW_DATE","AUTHOR","ISBN","DISCOUNTED_PRICE"],
	    ["1985/01/21","Douglas Adams",'0345391802',5.95],
	    ["1990/01/12","Douglas Hofstadter",'0465026567',9.95],
	    ["1998/07/15","Timothy \"The Parser\" Campbell",'0968411304',18.99],
	    ["1999/12/03","Richard Friedman",'0060630353',5.95],
	    ["2004/10/04","Randel Helms",'0879755725',4.50],
	    [conferencia,area,"0","0"],
	]
	si = StringIO.StringIO()
	cw = csv.writer(si)
	cw.writerows(data)
	output = make_response(si.getvalue())

	return output


