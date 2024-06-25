import os

from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('usuario/index.html')

@app.get("/admin/panel")
def get_admin_panel():
    return render_template('administrador/index.html')

@app.get("/admin/usuarios")
def get_admin_usuarios():
    return render_template('administrador/usuarios.html')

@app.get("/registro-saco")
def get_registro_saco():
    return render_template('usuario/registro-saco.html')

@app.get("/registro-bolsa")
def get_registro_bolsa():
    return render_template('usuario/registro-bolsa.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
