FROM python:3.9

COPY . app

WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install jupyter -U && pip install jupyterlab
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download "fr_core_news_sm"

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
