from app import create_app
app = create_app()
print(app.config['SECRET_KEY'])

if __name__=='__main__':
    app.run()