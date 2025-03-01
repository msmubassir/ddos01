# app.py
from flask import Flask, render_template, request
import subprocess
from rddos_tool import RDDoS

app = Flask(__name__)
rddos = RDDoS()

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        option = request.form.get('option')
        if option == '1':
            domain = request.form.get('domain')
            try:
                rddos.start_ddos(domain)
                result = f"DDoS attack started on {domain}"
            except Exception as e:
                result = f"Error: {e}"
        elif option == '2':
            ip = request.form.get('ip')
            try:
                rddos.start_ddos(ip)
                result = f"DDoS attack started on {ip}"
            except Exception as e:
                result = f"Error: {e}"
        elif option == '3':
            result = rddos.about()
        elif option == '4':
            return "Exiting..."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
