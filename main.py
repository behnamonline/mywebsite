from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html dir="rtl" lang="fa">
    <head>
        <meta charset="UTF-8">
        <title>وب‌سایت FastAPI</title>
        <style>
            body {
                font-family: Tahoma, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f4f9;
            }
            .container {
                text-align: center;
                padding: 2rem;
                background: white;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            h1 { color: #2c3e50; }
            p { color: #7f8c8d; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>بهنام آنلاین🚀</h1>
            <p>این یک برنامه ساده با FastAPI و آماده دپلوی روی Railway است.</p>
        </div>
    </body>
    </html>
    """

@app.get("/health")
def health_check():
    return {"status": "ok"}
