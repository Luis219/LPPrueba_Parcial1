
from markupsafe import escape

from flask import Flask, render_template, request, flash, url_for

app=Flask(__name__, template_folder='templates')


#ruta de la pagina index
@app.route('/')

#funcion que renderiza la pagina index.html
def inicio():
    return render_template('index.html')

#ruta de la pagina registro
@app.route('/registro', methods=['POST'])

#funcion que renderiza la pagina estadocliente.html
def registro():
    return render_template('estadocliente.html')

#ruta de la pagina registro
@app.route('/enviar', methods=['POST'])

#funcion que renderiza la pagina estadocliente.html
def enviar():
    nombre=request.form.get('nombre')
    telefono=request.form.get('telefono')
    estado=request.form.get('estado')

    nombres=[]
    telefonos=[]
    estados=[]

    nombres.append(nombre)
    telefonos.append(telefono)
    estados.append(estado)

    return render_template('estadocliente.html', nombres=nombres, telefonos=telefonos, estados=estados)

#ruta de la pagina index
@app.route('/tienda', methods=['POST'])

#funcion que renderiza la pagina tienda.html
def registro():
    return render_template('tienda.html')

#ruta de la pagina index
@app.route('/enviar_tienda', methods=['POST'])

#funcion que renderiza la pagina tienda.html
def enviarTienda():
    nombre=request.form.get('nombre')
    telefono=request.form.get('telefono')
    estado=request.form.get('estado')
    gerente=request.form.get('gerente')

    nombres=[]
    telefonos=[]
    estados=[]
    gerentes=[]

    nombres.append(nombre)
    telefonos.append(telefono)
    estados.append(estado)
    gerentes.append(gerente)

    return render_template('tienda.html', nombres=nombres, telefonos=telefonos, estados=estados, gerentes=gerentes)





#metodo principal
if __name__=='__main__':
    app.run(debug=True)




