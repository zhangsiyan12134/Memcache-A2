from app import backendapp
from dotenv import load_dotenv
if __name__ == '__main__':
    load_dotenv(verbose=True)
    backendapp.run(host='0.0.0.0', port=5001, debug=False)
