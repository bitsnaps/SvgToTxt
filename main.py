from typing import Union
from fastapi import FastAPI
#from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse
import lxml.etree as ET

app = FastAPI()

#app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Default root endpoint
@app.get("/")
async def home():
  return FileResponse('index.html')

@app.post("/upload")
def upload(file: Union[UploadFile,  None] = None):
  texts = ''
  try:
    if not file:
       texts = "No upload file sent"
    else:
        contents = file.file.read()
        # with open(f"./uploads/{file.filename}", 'wb') as f:
        #  f.write(contents)

        # Parse SVG data
        root = ET.fromstring(contents)
        # Extract all text (this will extract text in all level nodes)
        texts = [element for element in root.xpath('//text()') if element.strip()]

        # Save text into a TXT file
        #with open('output.txt', 'w') as file:
        #    file.write('\n'.join(texts))

  except Exception as e:
    return {"message": f"There was an error uploading the file: {e.message}"}
  
  finally:
    file.file.close()

    output = "<br>".join(texts)
    html_content = f"""
        <html>
            <head>
                <title>Output</title>
            </head>
            <body>
                <div id="output">{output}</h1>
            </body>
        </html>
        """
  return HTMLResponse(content=html_content, status_code=200)
