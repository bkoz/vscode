Using vscode with python on Openshift

```
oc new-app python-test

oc new-app --template=postgresql-ephemeral -p POSTGRESQL_USER=postgresql -p POSTGRESQL_PASSWORD=postgresql -p POSTGRESQL_DATABASE=sampledb

oc rsync data postgresql-1-878q8:/var/tmp

oc rsh postgresql-podtutorial.com/postgresql-administration/postgresql-create-database/)
```

Connect
```
psql $POSTGRESQL_DATABASE $POSTGRESQL_USER
```
To manually create a database and a table see the 
[tutorial](https://www.postgresqltutorial.com/postgresql-administration/postgresql-create-database/)

Works but errors out
```
pg_restore -U $POSTGRESQL_USER -d $POSTGRESQL_DATABASE /var/tmp/data/dvdrental.tar
```
Misc admin commands
```
\l
\db
\dt
```

Silent but creates tables
```
pg_restore -U $POSTGRESQL_USER  -P $POSTGRESQL_PASSWORD -d $POSTGRESQL_DATABASE /var/tmp/data/dvdrental.tar
```

Pod Debugging
```
oc rsh postgres-pod
psql $POSTGRESQL_DATABASE $POSTGRESQL_USER
default=> \dt
default=> select * from welcome_pageview;
```

```
