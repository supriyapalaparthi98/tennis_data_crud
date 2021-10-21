FROM python:3.8.4-buster
WORKDIR /code
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]