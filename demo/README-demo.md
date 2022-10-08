Using vscode with python on Openshift

See the `demo` directory for a simple app that connects 
to postgresql then logs and returns the host address. 
Service discovery is provided via environment variables.



Login to an Openshift cluster

In the upper right menu under your name, choose `Copy Login Command` and 
copy the `server URL` and `token` from the example `oc` command string.

Launch vscode.

Choose the Openshift Connector Extension

Login to an Openshift cluster

Provide the cluster URL and token to vscode

Right click the server connection and choose `New Project`

Right click the project and choose `New Component`

Select a workspace context directory 

Select a python/flask workspace component

Provide a name for the component.

Right click the app name and `push` it.

It should push your code (app.py) and create a route.







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
