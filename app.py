from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        option = request.form.get('option')
        if option == '1':
            domain = request.form.get('domain')
            try:
                import socket
                ip = socket.gethostbyname(domain)
                result = f"Resolved IP for {domain}: {ip}"
            except Exception as e:
                result = f"Error: {e}"
        elif option == '2':
            ip = request.form.get('ip')
            result = f"You entered IP: {ip}"
        elif option == '3':
            result = """
            RedDDoS Tool is an open source tool for penetration.
            You can test networks/servers/any other devices with it.
            Author of the program is not responsible for its usage.
            """
        elif option == '4':
            result = "Exiting..."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
