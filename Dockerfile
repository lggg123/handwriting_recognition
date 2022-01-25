FROM tensorflow/tensorflow

COPY . /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
EXPOSE 8000:8000
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]