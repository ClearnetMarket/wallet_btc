from flask import jsonify
from app.scripts import\
    account_checker,\
    wallet_checkincomming,\
    wallet_deletewalletwork,\
    wallet_generateaddresses,\
    wallet_getnewaddress,\
    wallet_send
from app import app


@app.route('/', methods=['GET'])
def get_wallet_status():
    """
    Check to see if server is online
    :return:
    """

    return jsonify({
        "wallet_status": 'Bitcoin is Online',
    })


@app.route('/deletework', methods=['GET'])
def delete_work():
    """
    This will delete work or old db entries
    :return:
    """
    
    wallet_deletewalletwork.deleteoldorder()
    
    return jsonify({
        "status": 'Deleted Work',
    })
    
    
@app.route('/generateaddresses', methods=['GET'])
def generate_addresses():
    """
    This will generate addresses if it gets low or ignore if enough
    :return:
    """
    
    wallet_generateaddresses.generate_addresses()
    
    return jsonify({
        "status": 'Generated Addresses',
    })
    
    
@app.route('/send', methods=['GET'])
def send_coin():
    """
    send coin offsite
    :return:
    """
    
    wallet_send.mainquery()
    
    return jsonify({
        "status": 'sent coin',
    })

@app.route('/recieve', methods=['GET'])
def recieve_coin():
    """
    check for incomming bitcoin
    :return:
    """
    wallet_checkincomming.main()
    
    return jsonify({
        "status": 'checked for new coin',
    })



@app.route('/checkaccounts', methods=['GET'])
def check_accounts():
    """
    This will check accounts to make sure no empty addresses
    :return:
    """
    
    account_checker.main()
    
    return jsonify({
        "status": 'Checked Accounts',
    })

