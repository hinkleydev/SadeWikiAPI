from flask import Blueprint, redirect, request, jsonify
import requests, os

token = Blueprint("token", __name__)

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]

@token.get("/auth")
def redirect_auth():
    return redirect("https://github.com/login/oauth/authorize?scope=repo&client_id=" + CLIENT_ID)

@token.get("/callback")
def authenticate():
    code = request.args["code"]
    r = requests.post("https://github.com/login/oauth/access_token", 
        json={"client_id" : CLIENT_ID, "client_secret" : CLIENT_SECRET, "code" : code},
        headers={"accept" : "application/json"})
    return jsonify(r.json())
