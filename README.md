# python-react-boilerplate
This boilerplate project demonstrates how to render VueJS components in a FastAPI web application using Jinja2.

## Overview
This project demonstrates how to integrate VueJS with a Flask & FastAPI web application using Jinja2. The core concept is to copy the static build output from the VueJS project into the static resources folder of the Spring Boot application. React components are rendered by attaching multiple root elements to corresponding HTML DOM nodes, each identified by an `section-*` prefix.

## Technologies
* Backend
  * FastAPI
  * Jinja2
* Frontend
  * Vue

## Requirements
* Python 3.12+
* Node 20+

## Project Structure
* vue-common
  * A common Vue project that copies its build output to both `fastapi-vue`.
* fastapi-vue
  * A Python-based FlaskAPI project that uses the build output from `vue-common`.

## Run Instruction
### Overview
You can run either the FastAPI project, depending on your preference.

### Frontend
Default server port: 3000
```bash
npm install -g yarn # If yarn is not installed

cd react-common
yarn install
yarn build  # or `yarn serve` for dev mode (when USE_VUE_BUNDLE = False)
```

### Backend Environment Setup (Optional)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Backend (FastAPI)
* Default server port: 8000

```bash
cd fastapi-react
pip3 install -r requirements.txt
start.bat
```

## Related Projects
* https://github.com/rheech/spring-boot-react-boilerplate
* https://github.com/trinity-teaparty/spring-boot-vue-boilerplate