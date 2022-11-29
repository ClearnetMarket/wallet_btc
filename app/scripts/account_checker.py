
from app import db
from app.classes.wallet_btc import\
    Btc_Wallet,\
    Btc_WalletAddresses,\
    Btc_Unconfirmed
from app.classes.auth import Auth_User


def btc_get_address(userswallet):
    """
    if user has a wallet but no address
    get the user an unused address
    :param userswallet:
    :return:
    """

    print("user id has no address: ", userswallet.user_id)

    # sets users wallet with this address
    getnewaddress = db.session\
        .query(Btc_WalletAddresses)\
        .filter(Btc_WalletAddresses.status == 0)\
        .first()
    userswallet.address1 = getnewaddress.btcaddress
    userswallet.address1status = 1
    # update address in listing as used
    getnewaddress.status = 1

    db.session.add(userswallet)
    db.session.add(getnewaddress)

    print("adding an address to the wallet", getnewaddress.btcaddress)


def btc_create_wallet(user_id):
    """
    if no address or wallet!
    :param user_id:
    :return:
    """

    getnewaddress = db.session\
        .query(Btc_WalletAddresses)\
        .filter(Btc_WalletAddresses.status == 0)\
        .first()

    # if user has no wallet in database
    # create it and give it an address
    print("user id has no address OR WALLET..failure somewhere!: ", user_id)
    print("fixing problem")
    # create a new wallet
    btc_cash_walletcreate = Btc_Wallet(user_id=user_id,
                                      currentbalance=0,
                                      unconfirmed=0,
                                      address1=getnewaddress.btcaddress,
                                      address1status=1,
                                      address2='',
                                      address2status=0,
                                      address3='',
                                      address3status=0,
                                      locked=0,
                                      transactioncount=0
                                      )
    # add an unconfirmed
    btc_cash_newunconfirmed = Btc_Unconfirmed(
        user_id=user_id,
        unconfirmed1=0,
        unconfirmed2=0,
        unconfirmed3=0,
        unconfirmed4=0,
        unconfirmed5=0,
        txid1='',
        txid2='',
        txid3='',
        txid4='',
        txid5='',
    )
    getnewaddress.status = 1

    db.session.add(getnewaddress)
    db.session.add(btc_cash_walletcreate)
    db.session.add(btc_cash_newunconfirmed)

    print("created wallet:", getnewaddress.btcaddress)


def main():
    """
    Gets all users see if wallet is ok.
    If not redirects it

    :return:
    """
    getusers = db.session\
        .query(Auth_User)\
        .all()

    total_amount = 0

    for f in getusers:
        userswallet = db.session\
            .query(Btc_Wallet)\
            .filter(f.id == Btc_Wallet.user_id)\
            .first()
        if not userswallet:
            btc_create_wallet(user_id=f.user_id)
            total_amount = total_amount + 1
        if not userswallet.address1.startswith('3'):
            btc_get_address(userswallet)
            total_amount = total_amount + 1

    if total_amount > 0:
        db.session.commit()


if __name__ == '__main__':
    main()
