from fastapi  import FastAPI, params, Request
from database import database_client
from messages_template import messages, error_messages
from models.help_model import *


app = FastAPI()

@app.post("/api/help")
async def helper(req: Request) -> dict:
    body     = await req.body()
    response = help_handler(body)
    return {
        "text": response,
    }

#This is only for connection testing propouses
@app.post("/api/test")
def testApp() -> dict:
    message = messages.get('test')
    return {"text":message}

@app.post("/api/task")
async def task(req: Request) -> dict:
    body     = await req.body()
    response = database_client.add_task(body)

    if response['code'] == 200:
        return {"text":response['message']}
    else:
        return {'text':'an error'}

@app.post("/api/tasks")
async def task(req: Request) -> dict:
    body     = await req.body()
    response = database_client.get_tasks(body)
    response_text = ''

    for item in response['data']:
        response_text += item+'\n'

    if response['code'] == 200:
        return {"text":response_text}
    else:
        return {'text':'an error'}
