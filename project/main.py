from website import create_app

# creates the webserver
app = create_app()

# starts the webserver
if __name__ == '__main__':
    app.run(debug=True)
