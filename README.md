# TODO Website
Simple todo web application with django


## Steps

Clone this repository
```bash
git clone https://github.com/<your-name>/todo-app.git
```

Cd into the project
```
cd todo-app
```

Create virtual environment named env
```bash
python -m venv venv
```

> When used from within a virtual environment, common installation tools such as pip will install Python packages into a virtual 
> environment without needing to be told to do so explicitly

[Read more](https://docs.python.org/3/library/venv.html)

Activate virtual environment
```bash
.\venv\Scripts\activate
```

Install requirements
```bash
pip install -r requirements.txt
```

Create an app directory
```bash
mkdir app
```

Create django project (**todo is the name of the djangoproject app** and **app is the directory** you have created earlier)
```bash
django-admin startproject todo app
```
