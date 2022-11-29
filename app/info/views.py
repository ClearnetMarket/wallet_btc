from flask import jsonify, Response
from app.info import info


# End Models


@info.route('/status', methods=['GET'])
def vendor_topbar_get_issues_count():
    """
    Gets the count of vendor order issues.  Notification bar at top
    :return:
    """
    return jsonify({
        "wallet_status": 'not yet set up',
    })
