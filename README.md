Using vscode with python on Openshift

```
oc new-app python-test

oc new-app --template=postgresql-ephemeral -p POSTGRESQL_USER=postgresql -p POSTGRESQL_PASSWORD=postgresql -p POSTGRESQL_DATABASE=sampledb

oc rsync data postgresql-1-878q8:/var/tmp

oc rsh postgresql-pod

Connect
psql $POSTGRESQL_DATABASE $POSTGRESQL_USER

Works but errors out
pg_restore -U $POSTGRESQL_USER -d $POSTGRESQL_DATABASE /var/tmp/data/dvdrental.tar

Show databases
default=> \l

Confirm there are tables and rows.
psql $POSTGRESQL_DATABASE $POSTGRESQL_USER
default=> \dt

Silent but creates tables
pg_restore -U $POSTGRESQL_USER  -P $POSTGRESQL_PASSWORD -d $POSTGRESQL_DATABASE /var/tmp/data/dvdrental.tar

Pod Debugging
oc rsh postgres-pod
psql $POSTGRESQL_DATABASE $POSTGRESQL_USER
default=> \dt
default=> select * from welcome_pageview;


```
