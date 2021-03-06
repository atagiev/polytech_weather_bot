FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/"

ENTRYPOINT ["python"]

CMD ["src/main.py"]