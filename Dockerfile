FROM python:3.10-slim
WORKDIR /app
COPY behavioral-threat-intel behavioral-threat-intel
RUN pip install --no-cache-dir -r behavioral-threat-intel/requirements.txt
EXPOSE 8000
CMD ["uvicorn", "behavioral-threat-intel.api_server:app", "--host", "0.0.0.0", "--port", "8000"]
