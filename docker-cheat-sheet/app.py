from flask import Flask, Response
import requests
import datetime
import random

app = Flask(__name__)

@app.route('/<user>')
def hello_world(user):
    # Current server time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Call external API (GitHub)
    try:
        response = requests.get("https://api.github.com")
        api_status = response.status_code
    except:
        api_status = "Failed to reach API"
    
    # Funny messages
    funny_messages = [
        "Did you bring snacks? Because coding is hungry work! 🍕",
        "I tried to be normal once. Worst two minutes ever. 😎",
        "Keep calm and Docker on! 🐳",
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"
    ]
    
    random_funny = random.choice(funny_messages)
    
    # HTML content with improved styling
    html_content = f"""
    <html>
        <head>
            <title>Docker + Flask Fun</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background-color: #f0f8ff;
                    padding-top: 50px;
                }}
                h1 {{
                    font-size: 60px;
                    font-weight: bold;
                    color: #333;
                }}
                p.funny {{
                    font-size: 28px;
                    font-weight: bold;
                    color: #0077cc;
                    margin-top: 20px;
                }}
                p.info {{
                    font-size: 22px;
                    color: #555;
                    margin-top: 15px;
                }}
            </style>
        </head>
        <body>
            <h1>Hello, {user}! 😁</h1>
            <p class="funny">{random_funny}</p>
            <p class="info">
                Server time: {current_time} <br>
                GitHub API status: {api_status}
            </p>
        </body>
    </html>
    """
    
    return Response(html_content, mimetype='text/html')

@app.route('/')
def default_user():
    return hello_world("Guest")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
