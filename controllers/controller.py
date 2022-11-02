from flask import render_template
from app import app
from models.order_list import order_list

# @app.route('/')
# def index():
#     return "Hello World!"

@app.route('/orders')
def order():
    return render_template('index.html', title='Home', order_list=order_list)

@app.route('/orders/<index>')
def order_full(index):
    return render_template('orders.html', title='Home', order_list=order_list[int(index)-1], index=index)