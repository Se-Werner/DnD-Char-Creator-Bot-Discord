FROM balenalib/raspberry-pi-debian-python:latest

WORKDIR /usr/scr/app

RUN pip install discord.py dotenv

COPY dnd_lines.txt .
COPY main.py .

CMD ["python", "main.py"]