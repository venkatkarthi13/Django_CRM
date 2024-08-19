from waitress import serve
from CRM_App.wsgi import application  # Adjust the import according to your project structure

if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=8000)
