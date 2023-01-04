from website import create_app

app = create_app() # creates the webserver

if __name__ == '__main__':
    app.run(debug=True)         # starts the webserver


