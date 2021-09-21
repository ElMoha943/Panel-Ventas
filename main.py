from website import create_app

# CREA LA APP DE FLASK Y LA EJECUTA
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=80)