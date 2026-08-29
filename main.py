from fastapi import FastAPI ,UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from inference import predict

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home ():
    return{"message":"classifir digit "}

@app.post("/predicit")
async def predicition(file:UploadFile=File(...)):
    img = Image.open(file.file)
    pred = predict(img)
    return{"prediction":pred}



