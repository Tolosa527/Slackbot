from google.cloud import datastore
from datetime import datetime
from messages_template import messages, error_messages

datastore_client = datastore.Client()

def add_task(body):

    if not body:
        return  {
            'code':404,
            'message': error_messages.get('body_is_empty')
        }

    dateTimeObj  = datetime.now()
    created_date = dateTimeObj.strftime("%d-%b-%Y")
    created_time = dateTimeObj.strftime("%H:%M:%S")
    text         = str(body).split('&')[8].split("=").pop(1)
    user         = str(body).split('&')[6].split("=").pop(1)
    lw_text      = text.lower()
    state        = True
    key          = datastore_client.key(user)

    entity = datastore.Entity(key=key)
    entity['created_date'] = created_date
    entity['created_time'] = created_time
    entity['text']         = text
    entity['state']        = state

    # I have to improve this try-except
    try:
        datastore_client.put(entity)
    except Exception as e:
        print(e)
        code = str(e).split(' ').pop(0)
        return {
            'code': code,
            'message': e.message
        }

    return {
        'code':200,
        'message': 'added'#messages.get('Entity was added')
    }

# this method returns all the task
# for the user that is execution the query
def get_tasks(body):
    if not body:
        return  {
            'code':404,
            'message': error_messages.get('body_is_empty')
        }

    result_list = []
    user        = str(body).split('&')[6].split("=").pop(1)
    query       = datastore_client.query(kind=user)
    results     = list(query.fetch())

    # In this for we create the result dictionary
    for entity in results:
        print(entity['text'])
        if entity['state'] == True:
            date = entity['created_date']
            time = entity['created_time']
            text = entity['text'].replace('+',' ')
            result_list.append(time +' '+ date+': '+text)

    return {
        'code':200,
        'data':result_list
    }
