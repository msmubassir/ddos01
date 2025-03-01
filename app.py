from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle user input
        option = request.form.get('option')
        if option == '1':
            domain = request.form.get('domain')
            try:
                import socket
                ip = socket.gethostbyname(domain)
                result = f"Resolved IP for {domain}: {ip}"
            except Exception as e:
                result = f"Error: {e}"
            return render_template('index.html', result=result)
        elif option == '2':
            ip = request.form.get('ip')
            result = f"You entered IP: {ip}"
            return render_template('index.html', result=result)
        elif option == '3':
            about_text = """
            RedDDoS Tool is an open source tool for penetration.
            You can test networks/servers/any other devices with it.
            Author of the program is not responsible for its usage.
            """
            return render_template('index.html', result=about_text)
        elif option == '4':
            return "Exiting..."
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
