# Verifica file di testo

>Flask

Applicazione che verifica i file di testo prodotti dal software di contabilità

Procedura di attivazione:

1. python -m venv env
2. source env/bin/activate
3. pip install -r requirements.txt
4. python -m flask run
oppure
python -m flask run --host=0.0.0.0 (IP)
5. in caso di problemi di codifica (testato su server CentOS):
export LC_ALL=it_IT.UTF-8
export LANG=it_IT.UTF-8
