FROM python:3
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY customers.txt .
COPY distance_invite.py .
COPY run_invites.py .
COPY tests.py .
COPY config.yml .

COPY ./run.sh /run.sh
RUN chmod -R 777 /run.sh
ENTRYPOINT ["/run.sh"]
