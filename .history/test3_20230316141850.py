from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# ユーザーの情報を格納するための仮のデータベース
users = {'admin': {'password': 'adminpassword'},
         'user1': {'password': 'user1password'},
         'user2': {'password': 'user2password'}}

# UserMixin を継承した User クラスを定義
class User(UserMixin):
    pass

# ユーザーIDからユーザーオブジェクトを取得する関数
@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        user = User()
        user.id = user_id
        return user
    return None

# ログインページのルーティング
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and password == users[username]['password']:
            user = User()
            user.id = username
            login_user(user)
            return redirect(url_for('home'))
        else:
            return 'Invalid username/password combination'
    else:
        return render_template('login.html')

# ログアウトのルーティング
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# ホームページのルーティング
@app.route('/')
@login_required
def home():
    return f'Hello, {current_user.id}! This is the home page.'

if __name__ == '__main__':
    app.run(debug=True)
