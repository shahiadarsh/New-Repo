from flask import Flask, render_template
import getpass
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def display_info():
    # a. Your full name
    full_name = "Your Full Name"  # Replace with your actual full name

    # b. System username
    username = getpass.getuser()

    # c. Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # d. Top output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
    except subprocess.CalledProcessError:
        top_output = "Error running top command."

    return render_template('index.html', 
                          name='Adarsh Shahi', 
                          username="shahiadarsh", 
                          server_time="2024-10-18 17:7:27.513300", 
                          top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)