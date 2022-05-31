
from flask import Flask, render_template

app=Flask(__name__, template_folder='templates')


#ruta de la pagina index
@app.route('/')

#funcion que renderiza la pagina index.html
def inicio():
    return render_template('index.html')

#metodo principal
if __name__=='__main__':
    app.run(debug=True)




