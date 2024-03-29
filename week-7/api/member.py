from flask import Blueprint, jsonify, request, session
from decorators import with_cnx

blueprint_member_api = Blueprint('member_api', __name__)

@with_cnx(need_commit = True)
def updateMemberData(cursor, user_name, user_id):
  cursor.execute('UPDATE member SET name = %s WHERE username = %s', (user_name, user_id))

@blueprint_member_api.route('/member', methods=['POST'])
def memberApi():
  user_name = request.get_json()['userName']
  if 'user_id' in session and user_name:
    updateMemberData(user_name, session.get('user_id'))
    return jsonify({ 'ok': True })
  else:
    return jsonify({ 'error': True })