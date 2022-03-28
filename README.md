# github-monitor
Monitor de repositórios via rest API

#### Pré-requisitos:	
* Python 3.10.0

#### Configurando projeto
```bash
$ git clone git@github.com:marcelinoavelar/github-monitor.git
$ cd github-monitor
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
``` 

#### Executando testes
```bash
$ make test
``` 

#### Listar opções para enviar ou agendar um hook via linha de comando
```bash
$ python main.py -h
``` 

#### Inicializar api rest.
```bash
$ uvicorn server:app --reload
``` 
Acesse no seu navegador [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) e veja a documentação da API

#### Executar hooks agendados
```bash
$ python job.py
``` 