FROM python:3.8

# Set environment variables
ENV GEMINI_API_KEY = "AIzaSyBf4aeXhaa6A8qqY1dRV_9C-Xp5JPrH0pY"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run the Streamlit app
CMD ["streamlit", "run", "main.py"]