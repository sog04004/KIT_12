from flask import Flask, request, render_template, redirect, url_for, abort, session
import dbdb

app = Flask(__name__)

app.secret_key = b'aaa!111/'

@app.route('/')
def index():
    return '메인페이지'
    
# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        print(dbdb.get_pw(id))
        if id != None and dbdb.get_pw(id) == pw:
            session['user'] = id
            return '''
                <script> alert("안녕하세요~ {}님");
                location.href="/form"
                </script>
            '''.format(id)
        else:
            return "아이디 또는 패스워드를 확인 하세요."

# 로그아웃(session 제거)
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('form'))
    
# 로그인 사용자만 접근 가능으로 만들면
@app.route('/form') 
def form():
    if 'user' in session:
        return render_template('test.html')
    return redirect(url_for('login'))

@app.route('/join', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        id = request.form["id"]
        pw = request.form["pw"]
        if id == '' or pw == '':
            return '아이디와 비밀번호를 입력 해주세요.'
        if dbdb.select_id(id) == None:
            dbdb.insert_data(id, pw)
            return '아이디: {} 비밀번호: {} 가입완료'.format(id, pw)
        else:
            return '이미 가입한 아이디 입니다.'

@app.route('/getinfo')
def getinfo():
    ret = dbdb.select_all()
    return render_template('getinfo.html', data=ret)

if __name__ == '__main__':
    app.run(debug=True)
