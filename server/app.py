FROM python:3.9

WORKDIR /code


COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip install fastapi uvicorn

COPY . .


EXPOSE 7860


CMD ["python", "server/app.py"]