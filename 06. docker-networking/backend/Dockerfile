FROM tensorflow/tensorflow

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install transformers Flask nltk tinydb

RUN python preparation.py 

EXPOSE 3000

CMD ["python", "app.py"]

