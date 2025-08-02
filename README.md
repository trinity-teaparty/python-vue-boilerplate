# python-vue-boilerplate
This boilerplate project demonstrates how to render VueJS components in a Flask & FastAPI web application using Jinja2.

## Overview
This project demonstrates how to integrate VueJS with a Flask & FastAPI web application using Jinja2. The core concept is to copy the static build output from the VueJS project into the static resources folder of the Spring Boot application. Vue components are rendered by attaching multiple root elements to corresponding HTML DOM nodes, each identified by an `section-*` prefix.

## Technologies
* Backend
  * Flask
  * FastAPI
  * Jinja2
* Frontend
  * Vue
  * TypeScript

## Requirements
* Python 3.10+
* Node 20+

## Project Structure
* vue-common
  * A common Vue project that copies its build output to both `flask-vue` and `fastapi-vue`.
* flask-vue
  * A Python-based Flask project that uses the build output from `vue-common`.
* fastapi-vue
  * A Python-based FlaskAPI project that uses the build output from `vue-common`.

## Run Instruction
### Overview
You can run either the Flask or FastAPI project, depending on your preference.

### Frontend
```bash
npm install -g yarn # If yarn is not installed

cd vue-common
yarn install
yarn build
```

### Backend Environment Setup (Optional)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Backend (Flask)
* Default server port: 5000

```bash
cd flask-vue
pip3 install -r requirements.txt
python3 main.py
```

### Backend (FastAPI)
* Default server port: 5000

```bash
cd fastapi-vue
pip3 install -r requirements.txt
python3 main.py
```

## Related Projects
* https://github.com/rheech/spring-boot-vue-boilerplate
* https://github.com/AkiaCode/python-react-boilerplate
* https://github.com/trinity-teaparty/spring-boot-vue-boilerplate
