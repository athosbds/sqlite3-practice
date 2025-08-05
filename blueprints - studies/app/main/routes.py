from flask import Flask, render_template
from . import main_bp

@main_bp.route('/')
def main_page():
    return render_template('home.html')