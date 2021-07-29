from config import Config
from flask import Flask, request
from flask_babel import Babel, lazy_gettext as _l
from flask_login import current_user, LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'  # used by @login_required
login.login_message = _l('Please log in to access this page')

migrate = Migrate(app, db)

# Climsoft DB
cdb = SQLAlchemy(app)
cdb.session.bind = db.get_engine(app, app.config.get('DEFAULT_CDMS'))


@babel.localeselector
def get_locale():
    if hasattr(current_user, 'language') and current_user.language:
        return current_user.language
    else:
        # Get web browser to determine the language
        return request.accept_languages.best_match(app.config['LANGUAGES'])


# Disable PEP8 warnings for delayed and unused imports
from app import routes, models  # noqa: E402, F401


from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension(app)
