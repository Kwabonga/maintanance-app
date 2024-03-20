from flask import Blueprint,render_template, request, flash, redirect, url_for, jsonify
from flask_login import  login_required,current_user
from . import db
from .models import User,Report
import json, smtplib, ssl
views=Blueprint('views',__name__)
@login_required
@views.route('/')
def home():
    return render_template("home.html", user=current_user)




