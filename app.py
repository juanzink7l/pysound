from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db
from routes.auth import auth_bp
from routes.songs import songs_bp
from routes.playlists import playlists_bp

def create_app():
    app = Flask(__name__)   
    app.url_map.strict_slashes = False

    # Configurações
    app.config['SECRET_KEY']            = 'pysound-senai-taguatinga-2024'
    app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///pysound.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY']        = 'jwt-super-secreto-senai'

    # Inicializa extensões
    db.init_app(app)
    JWTManager(app)
    CORS(app)   # Permite requisições de qualquer origem (importante para o front)

    # Registra os Blueprints (grupos de rotas)
    app.register_blueprint(auth_bp,      url_prefix='/auth')
    app.register_blueprint(songs_bp,     url_prefix='/songs')
    app.register_blueprint(playlists_bp, url_prefix='/playlists')

    # Interface visual de testes
    @app.route('/')
    def index():
        return render_template('index.html')

    # Cria as tabelas na primeira execução
    with app.app_context():
        db.create_all()
        seed_data(app)   # Popula com dados de exemplo

    return app

def seed_data(app):
    """Popula o banco com dados iniciais para demo"""
    from models import User, Song
    from werkzeug.security import generate_password_hash

    if User.query.first():
        return  # Já tem dados, não repete

    demo_user = User(username='admin', email='admin@pysound.com',
                     password=generate_password_hash('123456'))
    db.session.add(demo_user)
    db.session.flush()


    songs = [
        Song(title='Lugar ao sol', artist='Charlie Brown Jr', album='100% Charlie Brown Jr', genre='rock', duration='212', user_id=demo_user.id),
        Song(title='Vou me embriagar de você', artist='Charlie Brown Jr', album='La Familia 013', genre='rock', duration='264', user_id=demo_user.id),
        Song(title='Só existe o agora', artist='Charlie Brown Jr', album='Camisa 10 joga bola até na chuva', genre='rock', duration='268', user_id=demo_user.id),
        Song(title='I fell so good today', artist='Charlie Brown Jr', album='Imunidade Musical', genre='rock', duration='248', user_id=demo_user.id),
        Song(title='Só por uma noite', artist='Charlie Brown Jr', album='Bocas Ordinárias', genre='rock', duration='203', user_id=demo_user.id),
    ]
    db.session.add_all(songs)
    db.session.commit()
    print("Banco populado com dados de demo!")

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)





