# Development Guide

## Front-end

Required skills: [Vue](https://vuejs.org/), [Nuxt](https://nuxt.com/)

Project address: [https://github.com/hdrbv/yachat](https://github.com/hdrbv/yachat)

### Environment Setup
Install the latest stable version of node.js. If you need to package it as a docker image, you also need to install docker.

### Install dependencies

```
yarn install
```

### Start development server

```
yarn dev
```

### Build

```
yarn build
```

### Package as a docker image

```
docker build -t image-name:latest .
```


## Back-end

Required skills: [Python](https://www.python.org/), [Django](https://djangoproject.com/)

Project address: [https://github.com/hdrbv/yachat/back_end_server](https://github.com/hdrbv/yachat/back_end_server)

### Environment Setup
Install Python, pip/pipenv. If you need to package it as a docker image, you also need to install docker.

### Install dependencies

```
pip install -r requirements.txt
```

### Start development server

```
python manage.py runserver
```

### Package as a docker image

```
docker build -t image-name:latest .
```
