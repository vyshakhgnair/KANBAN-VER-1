
from flask import Flask, render_template, url_for, redirect, request,session,g
from model import *
import functools
from functools import wraps

error=None
@app.route('/',methods=['GET','POST'])
def login():
    if request.form:
        username = request.form['username']
        password = request.form.get('password')
        x = user.query.filter_by(user_name=username, user_password=password).first()
        if x is not None:
            session['user_id'] = x.user_id
            session['user_name']=x.user_name
            return redirect(url_for("dashboard"))
    return render_template('login.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        userpassword = request.form['password']
        userconpassword=request.form['conpassword']
        if userpassword==userconpassword:
            try:
                data = user(user_name=username,
                user_password=userpassword)
                db.session.add(data)
                db.session.commit()
            except db.IntegrityError:
                print("error")
            else:
                return render_template('success.html')
    return render_template('signup.html')

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    p=lists.query.filter_by(list_userid=session.get('user_id')).all()
    print(p)
    if p==[]:
        print("asdfasd")
        return render_template('basic-dashboard.html',usernm=session.get('user_name'))
    else:
        print(p)
        return render_template('signup.html')


@app.route('/addlist',methods=['GET','POST'])
def addlist():
    return render_template('dashboard.html')

@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    user_name=session.get('user_name')

    if user_id is None:
        g.user = None
    else:
        g.user = user.query.filter_by(user_id=user_id).first()
    print(session.get('user_id'))
    

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))

        return view(**kwargs)

    return wrapped_view
