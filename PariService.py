def add_pari(user_id, pari):
    message = "Добавлено пари \"" + pari + "\" для пользователя id=" + str(user_id)
    return message

def get_paris(user_id):
    return ["Test1", "Test2", "Test3"]

def set_pari_name():
    return "Введите название пари"

def set_pari_taker():
    return "С кем вы хотите заключить пари?"
def pari_created():
    return "Вы заключили пари"