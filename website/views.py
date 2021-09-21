from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import Producto
from . import db
import json, random

jsonText = {
 'Lunes' : 10,
 'Martes' : 11,
 'Miercoles' : 12,
 'Jueves' : 11,
 'Viernes' : 15
}

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
	products = Producto.query.all()
	if request.method == 'POST':
		if request.form.get('add') == 'Agregar':
		    name = request.form.get('Nombre')
		    price = request.form.get('Precio')
		    new = Producto(nombre=name, precio=price, stock=0)
		    db.session.add(new)
		    db.session.commit()
		    flash('Producto Añadido!', category='success')
		elif request.form.get('deleteall') == 'Eliminar':
			for me in products:
				db.session.delete(me)
			db.session.commit()
			flash('Producto Eliminado!', category='success')
		return redirect("/")
	else:
		return render_template("home.html", productos=products, user=current_user, data=jsonText)

@views.route('/delete/<int:id>')
def delete(id):
	borrar = Producto.query.get_or_404(id)
	try:
		db.session.delete(borrar)
		db.session.commit()
		print('Borrado Exitosamente')
	except Exception as e:
		print('Error')
	return redirect("/")

@views.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
	editar = Producto.query.get_or_404(id)
	if request.method == 'POST':
		try:
			editar.nombre = request.form.get('Nombre')
			editar.precio = request.form.get('Precio')
			db.session.commit()
			return redirect("/")
		except Exception as e:
			print('Error')
	else:
		return render_template("edit.html", name=editar.nombre, price=editar.precio, user=current_user, id=id)