## Installation:
This guide is designed for linux and mac but can easily be used on Windows.
This program is deigned for Python 3.
Install either through a virtualenv or thought your normal python install.
### Prerequisites
- python 3
[Install Python 3](https://www.python.org/downloads/)

- virtualenv
```
pip install virtualenv
```

- SQLite or PostgreSQL
[Install SQLite](http://www.tutorialspoint.com/sqlite/sqlite_installation.htm)
[Install PostgreSQL on Debian/Ubuntu Linux](http://www.stuartellis.eu/articles/postgresql-setup/)
[Install PostgreSQL on CentOS/RHEL Linux](https://wiki.postgresql.org/wiki/YUM_Installation)
[Install PostgreSQL on Mac](http://postgresapp.com/)

### Method A - Virtualenv SQLite with Tornado Web Server
Recommended installation method

1. download source code into avg_alpr directory
```
git clone https://gitlab.com/msemple1111/average_check.git avg_alpr
```

2. create the virtual environment and cd into it
```
virtualenv -p python3 avg_alpr
cd avg_alpr
```

3. Activate virtualenv
```
source bin/activate
```

4. Install Python Dependancys
```
pip install sqlite3 tornado flask uwsgi
```

5. Populate sqlite database
'''
sqlite3 average_check
'''
```
sqlite> .read create.sql
```

### Method B - Python 3


