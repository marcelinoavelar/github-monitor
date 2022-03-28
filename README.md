# github-monitor
Monitor de repositórios via rest API

#### Pré-requisitos:	
* Python 3.10.0

#### Configurando projeto
```bash
$ git clone https://github.com/marcelinoavelar/github-monitor.git
$ cd github-monitor
$ source .venv/bin/active
$ pip install -r queriments.txt
``` 

#### Executando testes
```bash
$ make test
``` 

#### Listar a opções para enviar ou agendar um hook via linha de comando
```bash
$ python main.py -h
``` 

#### Inicializar a api rest, execute os comando abaixo.
```bash
$ uvicorn server:app --reload
``` 
Acesse no seu navegador [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

#### Executar o hooks agendados
```bash
$ python job.py
``` 