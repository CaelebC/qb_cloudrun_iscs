FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8080
ENV PORT 8080
ENV HOST 0.0.0.0
WORKDIR /code
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
RUN ["chmod", "+x", "./entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]