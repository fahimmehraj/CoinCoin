from database import db

# model of user table from SQL database
class User(db.Model):
    userID = db.Column(db.String, primary_key=True, nullable=False)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    display_name = db.Column(db.VARCHAR(25), unique=True, nullable=False)
    coin_val = db.Column(db.Integer)
    offers = db.relationship('Offer', backref=db.backref("user"))


# model of Offers table from SQL database
class Offer(db.Model):
    offerID = db.Column(db.String, primary_key=True)
    coinCoinOffer = db.Column(db.Integer)
    USDOffer = db.Column(db.Float)
    display_name = db.Column(db.VARCHAR(25))
    userID = db.Column(db.Integer)
    userID = db.Column(db.Integer, db.ForeignKey(User.userID), nullable=False)

    def __repr__(self):
        return "Offer ID {} created, {} coincoins for ${} ".format(self.offerID, self.coinCoinOffer, self.USDOffer)

