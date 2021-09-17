from flask import Flask  

app = Flask(__name__, static_folder="components/assets", template_folder="boilerplate")