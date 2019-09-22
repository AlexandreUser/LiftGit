from flask import Flask, flash, redirect, render_template, request, session, url_for
from datetime import *
from pymongo import MongoClient
from flask import jsonify
import uuid
import os
from flask_api import status
import subprocess
import threading
import requests

app = Flask('project')
app.config['SECRET_KEY'] = 'random'
app.debug = True

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
      	return render_template("index.html")