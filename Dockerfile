FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy everything
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app/app.py"]

