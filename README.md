# README

## O que é essa aplicação?

- Uma aplicação desenvolvida em Python utilizando Flask.
- É uma aplicação Web com recursos simples porém que facilitam o entendimento dos conceitos durante o aprendizado de Docker e Kubernetes

## Como usar

### Criando um container

- Clone o repositório
```bash
# Crie uma virtualenv
cd flask-to-learn-containers/
# Fazer o build da imagem
docker image build -t flask-to-learn-containers .
# Criar um container expondo a porta de forma dinâmica
 docker container run -d -P flask-to-learn-containers
# Liste os containers e veja a porta em execução
docker container ls
# Abra o navegador utilizando o endereço de localhost
```

Exemplo: http://127.0.0.1:32770

`Lembre-se de mudar a porta de acordo com seu ambiente`

- Variáveis disponíveis:
  - COLOR = Muda o background
  - VERSION = Muda a versão