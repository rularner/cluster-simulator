FROM mysql:5.7.19
# Copy the database schema to the /data directory
ADD files/run_db files/init_db files/schema.sql /tmp/

# init_db will create the default
# database from epcis_schema.sql, then
# stop mysqld, and finally copy the /var/lib/mysql directory
# to default_mysql_db.tar.gz
USER mysql
# RUN /tmp/init_db

# run_db starts mysqld, but first it checks
# to see if the /var/lib/mysql directory is empty, if
# it is it is seeded with default_mysql_db.tar.gz before
# the mysql is fired up

# ENTRYPOINT "/tmp/run_db"