import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def get_list():
     return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    
def run():
    store.get_categories()

if __name__ == '__main__':
    run()