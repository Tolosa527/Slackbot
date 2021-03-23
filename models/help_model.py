from messages_template import messages, error_messages
from pydantic import BaseModel

def help_handler(body):

    response_message = ''
    text = str(body).split('&')[8].split("=").pop(1)
    lw_text = text.lower()

    help_dict_index = {
        'task': 'help_task',
        'remainder': 'help_remainder'
    }

    if lw_text in help_dict_index:
        index = help_dict_index[lw_text]
        response_message = messages.get(index)
    else:
        response_message = error_messages.get('command_not_found')

    return response_message