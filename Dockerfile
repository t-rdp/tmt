FROM python:3.11.0

COPY . /app
WORKDIR ./app
RUN pip install --upgrade setuptools -i https://pypi.doubanio.com/simple/
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple/
ENTRYPOINT ["python"]
CMD ["api.py"]