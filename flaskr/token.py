from flask import Blueprint, redirect, request, jsonify
import requests, os

token = Blueprint("token", __name__)

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]

@token.get("/auth")
def redirect_auth():
    return redirect("https://github.com/login/oauth/authorize?client_id=" + CLIENT_ID)

@token.get("/callback")
def authenticate():
    code = request.args["code"]
    r = requests.post("https://github.com/login/oauth/access_token", 
        json={"client_id" : CLIENT_ID, "client_secret" : CLIENT_SECRET, "code" : code},
        headers={"accept" : "application/json"})
    access_token = r.json()["access_token"]
    user = requests.get("https://api.github.com/user",
        headers={"Accept" : "application/json", "Content-Type" : "application/json", "Authorization" : "Bearer " + access_token})
    userValues = user.json()
    return jsonify({"user": userValues["login"], "token": access_token})
