import requests
from app import db
import app
from decimal import Decimal
from datetime import datetime
import json
from app.common.notification import create_notification
from app.common.functions import floating_decimals
from app.classes.wallet_btc import\
    Btc_Wallet,\
    Btc_TransactionsBtc,\
    Btc_WalletFee, \
    Btc_WalletWork
from app.classes.auth import Auth_User

def securitybeforesending(user, sendto, adjusted_amount):
    """
    # This function checks regex, amounts, and length of addrss
    """
    
    minamount = app.minamount
    maxamount = app.maxamount

    regexpasses = 1

    # test if length of address is ok
    if 24 <= len(sendto) <= 36:
        lengthofaddress = 1
    else:
        lengthofaddress = 0
        create_notification(username=user.display_name,
                     user_uuid=user.uuid,
                     msg="Incorrect wallet address when sending coin")

    # test to see if amount when adjusted is not too little or too much
    if Decimal(minamount) <= Decimal(adjusted_amount) <= Decimal(maxamount):
        amountcheck = 1
    else:
        amountcheck = 0
        create_notification(username=user.display_name,
                     user_uuid=user.uuid,
                     msg="Wallet didnt have enough coin to send.")

    # count amount to pass
    totalamounttopass = regexpasses + lengthofaddress + amountcheck

    if totalamounttopass == 3:
        itpasses = True
    else:
        itpasses = False

    return itpasses


def sendcoin(user, sendto, amount, comment):
    """
    # This function sends the coin off site
    """

    # variables
    dcurrency = app.digital_currency
    timestamp = datetime.utcnow()

    # get the fee from db
    getwallet = db.session\
        .query(Btc_WalletFee)\
        .filter_by(id=1)\
        .first()
    walletfee = getwallet.btc

    # get the users wall
    userswallet = db.session\
        .query(Btc_Wallet)\
        .filter_by(user_id=user.id)\
        .first()

    # proceed to see if balances check
    curbal = floating_decimals(userswallet.currentbalance, 8)
    amounttomod = floating_decimals(amount, 8)
    adjusted_amountadd = floating_decimals(amounttomod - walletfee, 8)
    adjusted_amount = floating_decimals(adjusted_amountadd, 8)

    sendto_str = str(sendto)
    final_amount_str = str(adjusted_amount)
    comment_str = str(comment)

    # double check user
    securetosend = securitybeforesending(user=user,
                                         sendto=sendto,
                                         adjusted_amount=adjusted_amount
                                         )
    if securetosend is False:
        create_notification(username=user.display_name,
                     user_uuid=user.uuid,
                     msg="Low Balance or incorrect address before sending.")
    else:

        # send call to rpc
        cmdsendcoin = sendcoincall(address=str(sendto_str),
                                   amount=str(final_amount_str),
                                   comment=str(comment_str)
                                   )

        # get the txid from json response
        print("sending a transaction..")
        print("txid: ", cmdsendcoin['result'])

        print("*"*15)
        txid = cmdsendcoin['result']

        # adds to transactions with txid and confirmed = 0 in order watch it
        trans = Btc_TransactionsBtc(
            category=2,
            user_id=user.id,
            confirmations=0,
            txid=txid,
            blockhash='',
            timeoft=0,
            timerecieved=0,
            otheraccount=0,
            address='',
            fee=walletfee,
            created=timestamp,
            commentbtc=comment_str,
            amount=amount,
            orderid=0,
            balance=curbal,
            confirmed=0,
            digital_currency=dcurrency
        )

        create_notification(username=user.display_name,
                     user_uuid=user.uuid,
                     msg="BTC has successfully been sent to destination.")

        db.session.add(userswallet)
        db.session.add(trans)



def mainquery():
    """
    # main query
    """
    work = db.session\
        .query(Btc_WalletWork) \
        .filter(Btc_WalletWork.type == 2) \
        .order_by(Btc_WalletWork.created.desc()) \
        .all()

    if work:
        for f in work:
            # off site
            if f.type == 2:
                user = db.session\
                .query(Auth_User)\
                .filter(Auth_User.id==work.user_id)\
                .first()
                sendcoin(user=user,
                         sendto=f.sendto,
                         amount=f.amount,
                         comment=f.txtcomment)
                f.type = 0

        db.session.commit()



def sendcoincall(address, amount, comment):

    # standard json header
    headers = {'content-type': 'application/json'}

    rpc_input = {
        "method": "sendtoaddress",
        "params":
            {"address": address,
             "amount": amount,
             "comment": comment,
             "subtractfeefromamount": True,
             }
    }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "1.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        app.url,
        data=json.dumps(rpc_input),
        headers=headers,
    )

    # the response in json
    response_json = response.json()

    return response_json

