from jogoteca import db

class Jogos(db.Model):
    id = db.Column(db.interger, primary_key=True, autoincremet=True)
    nome = db.Column(db.string(50), nullable=False)
    categoria = db.Column(db.string(40), nullable=False)
    console = db.Column(db.string(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
    

class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True, autoincremet=True)
    nome = db.Column(db.string(20), nullable=False)
    senha = db.Column(db.string(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name  