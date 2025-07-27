# python-react-boilerplate
This boilerplate project demonstrates how to render ReactJS components in a Flask & FastAPI web application using Jinja2.

## Overview
This project demonstrates how to integrate ReactJS with a Flask & FastAPI web application using Jinja2. The core concept is to copy the static build output from the ReactJS project into the static resources folder of the Spring Boot application. React components are rendered by attaching multiple root elements to corresponding HTML DOM nodes, each identified by an `section-*` prefix.

## Technologies
* Backend
  * Flask
  * FastAPI
  * Jinja2
* Frontend
  * React
  * TypeScript

## Requirements
* Python 3.10+
* Node 20+

## Project Structure
* react-common
  * A common React project that copies its build output to both `flask-react` and `fastapi-react`.
* flask-react
  * A Python-based Flask project that uses the build output from `react-common`.
* fastapi-react
  * A Python-based FlaskAPI project that uses the build output from `react-common`.

## Run Instruction
### Overview
You can run either the Flask or FastAPI project, depending on your preference.

### Frontend
```bash
npm install -g yarn # If yarn is not installed

cd react-common
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
cd flask-react
pip3 install -r requirements.txt
python3 main.py
```

### Backend (FastAPI)
* Default server port: 5000

```bash
cd fastapi-react
pip3 install -r requirements.txt
python3 main.py
```

## Related Projects
* https://github.com/rheech/spring-boot-react-boilerplate