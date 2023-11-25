from app import db

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Expense(id={self.id}, date={self.date}, category={self.category}, amount={self.amount})"