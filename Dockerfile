FROM python:3.11.0

COPY . /app
WORKDIR ./app
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api.py"]