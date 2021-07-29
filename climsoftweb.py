from app import app, cdb, db
from app import cli
from app.models import User

cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'cdb': cdb, 'db': db, 'User': User}