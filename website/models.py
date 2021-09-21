from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    monto = db.Column(db.Float)
    # productos = db.relationship('ProdVendidos', backref='venta', lazy=True)

# class ProdVendidos(db.Model):
#     venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'), nullable=False)
#     producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)