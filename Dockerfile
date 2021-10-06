FROM python:3.9

COPY . app

WORKDIR /app

RUN apt-get upgrade 
RUN apt-get update 
RUN apt-get -y install gcc
RUN apt-get -y install tesseract-ocr 
RUN apt-get -y install python-dev 
RUN apt-get -y install libxml2-dev 
RUN apt-get -y install libxslt1-dev 
RUN apt-get -y install antiword 
RUN apt-get -y install unrtf 
RUN apt-get -y install poppler-utils 
RUN apt-get -y install tesseract-ocr 
RUN apt-get -y install flac 
RUN apt-get -y install ffmpeg 
RUN apt-get -y install lame 
RUN apt-get -y install libmad0 
RUN apt-get -y install libsox-fmt-mp3 
RUN apt-get -y install sox 
RUN apt-get -y install libjpeg-dev 
RUN apt-get -y install swig 
RUN apt-get -y install libpulse-dev 

RUN pip install --upgrade pip
RUN pip install jupyter -U && pip install jupyterlab
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download "fr_core_news_sm"

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
