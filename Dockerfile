FROM python:3.12-slim
WORKDIR /app
RUN useradd --create-home appuser
COPY analisa_log.py auth.log ./
USER appuser
CMD ["python", "analisa_log.py", "auth.log"]
