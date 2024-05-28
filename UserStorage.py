user_dict = {}
def save_user(name,chatid):
    user_dict[name] = chatid
def get_user(name):
    return user_dict.get(name)