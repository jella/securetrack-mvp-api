from app import create_app
from flask import redirect

app = create_app()

@app.route('/')
def redirect_to_docs():
    return redirect('/openapi/swagger')


@app.route('/<int:id>')
def index(id: int):
    dados = {"nome": str(id)}
    return str(id)

if __name__ == '__main__':
    app.run(debug=True)
