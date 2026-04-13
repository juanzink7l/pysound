from flask import Flask, render_template
from flask__jwt_extend import JWTManager
from flask_cors import CORS
from models import db
from routes.auth import auth_bp
from routes.songs import songs_bp
from routes.playlists import playlists_bp


































