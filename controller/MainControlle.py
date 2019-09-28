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
from git import Repo,remote

app = Flask('project')
app.config['SECRET_KEY'] = 'random'
app.debug = True
@app.route("/show/repository", methods=["GET","POST"])
def showRepo():
	if request.method == "GET":
		path = request.args.get("path")
		myCmd = os.popen('cd '+path+' && ls').read()
		myCmd = myCmd.split("\n")
		return str(myCmd)
@app.route("/create/branch", methods=["GET","POST"])
def createBranch():
  if request.method == "POST":
    path = request.args.get("path")
    gitname = request.args.get("gitname")
    myCmd = os.popen("cd "+path+" && git checkout -b LiftGit && touch LIFTGIT.md && git add . && git commit -m 'configured lift'").read()
    repo = Repo(path)

    '''Enter code to commit the repository here.
    After commit run the following code to push the commit to remote repo.
    I am pushing to master branch here'''

    origin = repo.remote(name='origin')
    origin.push("LiftGit")

    return str(myCmd)

@app.route("/",methods=["GET","POST"])
def init():
    if request.method == "GET":
      	return render_template("form_wizards.html")

@app.route("/home",methods=["GET","POST"])
def index():
    if request.method == "GET":
      	return render_template("index.html")

@app.route("/add/repository",methods=["GET","POST"])
def addRepo():
    if request.method == "GET":
      	return render_template("form.html")