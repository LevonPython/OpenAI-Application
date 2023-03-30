1. Install PostgreSQL on your machine
```brew install postgresql
```

2. Once PostgreSQL is installed, you can use the psql command line interface to create a new database and user.

3. Open a terminal or command prompt window, and type the following command to connect to the default PostgreSQL database as the default user:

```psql postgres
```
31. Start the PostgreSQL server by running the following command:
```
pg_ctl -D /usr/local/var/postgres start
```
32. Verify that the PostgreSQL server is running by running the following command:
```ps auxwww | grep postgres
```
33. Once the PostgreSQL server is running, you can connect to it using the psql command line tool or another PostgreSQL client. To stop the PostgreSQL server, you can use the following command:
```
pg_ctl -D /usr/local/var/postgres stop
```
Note that the exact location of the PostgreSQL data files may vary depending on your installation. You can check the location of the data files by running the following command:
```pg_config --bindir
```
This command will show all running processes that contain the word "postgres". If the PostgreSQL server is running, you should see several processes with this name.
4. Once you are connected to the PostgreSQL server, you can create a new database and user using SQL commands.
To create a new database, use the CREATE DATABASE command, followed by the desired name of the database:
```CREATE DATABASE mydatabase;
```

This will create a new database with the name mydatabase.

To create a new user, use the CREATE USER command, followed by the desired username and password:

5. After creating the user, you need to grant appropriate privileges to the user for the new database. Use the GRANT command to do this:
```GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
```
This command grants all privileges on the mydatabase database to the myuser user.

6. Once you have created the database and user and granted privileges, you can exit the `psql` command line interface by typing `\q` or using the `CTRL-D` shortcut.

7. Finally, you can connect to the new database using the `psql` command line interface and the new user credentials:
```
psql -d mydatabase -U myuser -W
```

This command will connect to the `mydatabase` database as the myuser user, and prompt you to enter the password for the user. Once you have entered the password, you will be connected to the new database and can start using it.

8. \l lists all your databases
9. \connect database_name
10. grant usage on schema public to public;
grant create on schema public to public;
this gives all grants to make changes 
