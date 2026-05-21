from db import db

# давно не ліз в sqlalchemy..

order_items = db.Table(
    "order_items",
    db.Column("order_id", db.Integer, db.ForeignKey("order.id")),
    db.Column("menu_item_id", db.Integer, db.ForeignKey("menu_item.id"))
)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone_number = db.Column(db.String(15))


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    total_price = db.Column(db.Float)

    items = db.relationship("MenuItem", secondary=order_items)