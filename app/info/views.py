from flask import jsonify
from app.info import info
from app.scripts import wallet_info

# End Models


@info.route('/status', methods=['GET'])
def info_status():
    """
    See if info is online and ready
    :return:
    """
    
    return jsonify({
        "wallet_status": 'Ready for info',
    })



@info.route('/getbalance', methods=['GET'])
def get_balance():
    """
    Gets the balance of the wallet
    :return:
    """
    wallet_info.getthebalance()
    
    return jsonify({
        "wallet_status": 'Success',
    })



@info.route('/getwalletinfo', methods=['GET'])
def get_wallet_info():
    """
    Gets the wallet info
    :return:
    """
    wallet_info.getwalletinfo()
    
    return jsonify({
        "wallet_status": 'Success',
    })



@info.route('/listaccounts', methods=['GET'])
def list_accounts():
    """
    Gets the accounts
    :return:
    """
    
    wallet_info.listaccounts()
    
    return jsonify({
        "wallet_status": 'Success',
    })
