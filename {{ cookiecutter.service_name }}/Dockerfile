FROM python:3.6-slim

# Install dependencies
# Do this first for caching
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy
COPY experiments experiments
COPY {{ cookiecutter.package_name }} {{ cookiecutter.package_name }}
COPY logging.json logging.json

# Export ports
EXPOSE 5000

# Start app
CMD ["uvicorn", "{{ cookiecutter.package_name }}.app:app", "--host", "0.0.0.0", "--port", "5000"]