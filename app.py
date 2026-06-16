from flask import Flask, render_template, request, jsonify
from chatbot import get_chatbot_response
from database import register_user
from weather import get_weather
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from flask import (
    session,
    redirect,
    url_for
)
from database import (
    init_db,
    save_chat,
    get_chat_history,
    register_user,
    login_user,
    create_users_table
)

app = Flask(__name__)
app.secret_key = "crop-advisor"


# Initialize database
init_db()
create_users_table()

@app.route('/home')
def home():

    if 'user_id' not in session:
        return redirect('/')

    history = get_chat_history()

    return render_template(
        'index.html',
        history=history
    )

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    user_message = data.get('message', '')
    language = data.get('language', 'English')

    if not user_message:
        return jsonify({
            "response": "Please enter a message."
        })

    response = get_chatbot_response(
        user_message,
        language
    )

    save_chat(user_message, response)

    return jsonify({
        "response": response
    })

@app.route('/weather')
def weather():
    city = request.args.get('city')

    if not city:
        return jsonify({
            "error": "City is required"
        })

    result = get_weather(city)

    return jsonify(result)

@app.route('/history')
def history():
    chats = get_chat_history()
    return jsonify(chats)

@app.route("/crop/<crop_name>")
def crop_info(crop_name):
    pass

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        register_user(
            name,
            email,
            password
        )

        return redirect('/')

    return render_template('register.html')

@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        user = login_user(
            email,
            password
        )

        if user:

            session['user_id'] = user['id']
            session['name'] = user['name']

            return redirect('/home')

    return render_template('login.html')

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/technology')
def technology():
    return render_template('technology.html')

@app.route('/developer')
def developer():
    return render_template('developer.html')



if __name__ == "__main__":
    app.run(debug=True)