import requests

def telegram_packet_loss(bot_message):
    
    bot_token = '471642243:AAHpcIgobX_nbnOUEu6_Trs_EECydbmuJGU'
    bot_chatID = '-367341559'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

def telegram_lan(bot_message):
    
    bot_token = '471642243:AAHpcIgobX_nbnOUEu6_Trs_EECydbmuJGU'
    bot_chatID = '-358946380'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def telegram_wan_quocte(bot_message):
    
    bot_token = '471642243:AAHpcIgobX_nbnOUEu6_Trs_EECydbmuJGU'
    bot_chatID = '-334521942'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def telegram_wan_vccorp(bot_message):
    
    bot_token = '471642243:AAHpcIgobX_nbnOUEu6_Trs_EECydbmuJGU'
    bot_chatID = '-359400804'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def telegram_wan_vietnam(bot_message):
    
    bot_token = '471642243:AAHpcIgobX_nbnOUEu6_Trs_EECydbmuJGU'
    bot_chatID = '-332735157'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def telegram_network_error(bot_message):
    
    bot_token = '471642243:AAHpcIgobX_nbnOUEu6_Trs_EECydbmuJGU'
    bot_chatID = '-219641400'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()