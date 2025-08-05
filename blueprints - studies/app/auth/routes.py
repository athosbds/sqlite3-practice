from flask import Flask, render_template, redirect
from . import auth_bp
@auth_bp.route('/login')
def login():
    return render_template('login.html')
@auth_bp.route('/logout')
def logout():
    return render_template('logout.html')