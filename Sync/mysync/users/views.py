from flask import render_template,url_for,flash,redirect,request,Blueprint, jsonify, json
from mysync import app,db
from mysync.models import Item, List, User
from mysync.users.forms import SearchForm, LoginForm
print('coming')

user = Blueprint('user',__name__)

@user.route('/', methods=['GET','POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':

        loginid = form.username.data

        if form.login.data:
            validuser = User.query.all()
            for user in validuser:
                if loginid == user.userid:
                    return redirect(url_for('user.home',username=loginid))

            flash('User Not Registered!!')
            return redirect(url_for('user.login',form=form))

        if form.register.data:
            validuser = User.query.all()
            for user in validuser:
                if loginid == user.userid:
                    flash('User Already Registered!!')
                    return redirect(url_for('user.login',username=loginid))

            usr = User(userid=form.username.data)
            db.session.add(usr)
            db.session.commit()
            return redirect(url_for('user.home',username=loginid))

    return render_template('login.html',form=form)

@user.route('/home/<username>', methods=['GET','POST'])
def home(username):
    form = SearchForm()

    if form.validate_on_submit():

        if form.update.data:
            listitem = form.option.data
            chkitm = List.query.filter_by(username=username, listitem=listitem).all()
            for chk in chkitm:
                if listitem == chk.listitem:
                    flash('Item already present')
                    return redirect(url_for('user.home',username=username))

            lst = List(username=username,
                       listitem=form.option.data,
                       quantity=form.quantity.data)

            db.session.add(lst)
            db.session.commit()
            return redirect(url_for('user.home',username=username))

    list = List.query.filter_by(username=username).all()

    return render_template('home.html', form=form, list=list,username=username)

@user.route('/items')
def items():
    itm = Item.query.all()
    list_items = [r.as_dict() for r in itm]
    return jsonify(list_items)

@user.route('/dellistitem', methods=['GET','POST'])
def dellistitem():
    s = request.form['delitem']
    username = request.form['name']

    start = s.find(">") + len(">")
    end = s.find("</")
    substring = s[start:end]
    print(username)
    print(substring)
    deleteitem = List.query.filter_by(username=username, listitem=substring).first()

    db.session.delete(deleteitem)
    db.session.commit()

    return redirect(url_for('user.home',username=username))

@user.route("/logout")

def logout():

    return redirect(url_for('user.login'))
