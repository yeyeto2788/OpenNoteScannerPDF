# Use oficial image of python 3
FROM python:3.7
# Add all files from the repository.
COPY . /ons
# Set working directory to the one we've just copied.
WORKDIR /ons
# Install dependencies.
RUN pip install -r requirements.txt
# Define the entrypoint
ENTRYPOINT ["python"]
# Add the arguments we need to pass into the command above.
CMD ["run_server.py"]