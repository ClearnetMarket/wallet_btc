from app import db
from app.classes.wallet_btc import Btc_WalletWork


# run once every ten minutes
def deleteoldorder():

    getwork = db.session\
        .query(Btc_WalletWork)\
        .filter_by(type=0)\
        .all()
    if not getwork:
        print("no work!")
    else:
        for f in getwork:
            db.session.delete(f)
        db.session.commit()

if __name__ == '__main__':
    deleteoldorder()
