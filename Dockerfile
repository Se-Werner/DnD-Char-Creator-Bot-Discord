FROM balenalib/raspberry-pi-debian-python:latest

WORKDIR /usr/scr/app

RUN install_packages gcc \
    musl-dev \
    linux-headers \
    libc-dev

RUN python3 -m pip install discord.py --no-cache-dir
RUN python3 -m pip install python-dotenv --no-cache-dir

COPY dnd_lines.txt .
COPY main.py .

CMD ["python", "main.py"]