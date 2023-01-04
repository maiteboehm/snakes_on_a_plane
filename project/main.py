from website import create_app

#Creates the webserver
app = create_app()

#Starts the webserver
if __name__ == '__main__':
    app.run(debug=True)
