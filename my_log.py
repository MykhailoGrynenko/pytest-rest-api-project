import logging


print('i am a print')
logging.warning('i am a log')


"""

1. register - (username, password)
    :returns a useless token
    
2. login - (username, password)
    :returns TOKEN
    
3. get_user - (url, headers=TOKEN)
    :returns user data (user_id, username, ...)
    
4. delete_user - (url + user_id, headers=TOKEN)
    :returns 204

"""