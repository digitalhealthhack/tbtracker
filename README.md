# README for TB Tracker

This project was started at the [Spring Digital Health Oxford Hack Weekend in May 2016](http://hack.dhox.org).  The overall aim was to identify publicly available data related to TB / occurrence, extract, analyse and present in a useful format.

Steps needed to setup:

* Create virtualenv and add required python modules

```
$ pip install -r requirements.txt
``` 

* Create database and tables using sql provided in SQL directory

```
$ mysql

mysql> create database tbtracker;
mysql> create user 'tbtracker_user'@'localhost' identified by 'password';
mysql> grant all privileges on tbtracker.* to 'tbtracker_user'@'localhost';
mysql> flush privileges;

$ mysql tbtracker -u tbtracker_user -p < SQL/tbtracker_structure.sql

```

* Create config file and update credentials for new mysql user

```
$ cp config_example.yaml config.yaml
```

* Run scripts to extract data

```
$ ./extract_who_data.py
$ ./extract_worldbank_data.py
```