FROM python:3.8
WORKDIR /
COPY server ./server
RUN pwd
RUN ls -la
RUN pip install --no-cache-dir -r ./server/requirements.txt
EXPOSE 9898
CMD ["uvicorn", "server/app:app", "--host", "0.0.0.0", "--port", "9898"]

