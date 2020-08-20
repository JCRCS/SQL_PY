# SQL_PY
Is a repository that contains some mapping between SQL queries and python Development. 

* sql_table_parser
    * pretends to fetch all the tables that a SQL query depends on. In the particual case where is implemented is in the migration of a DWH to a HDFS based on CDP, where it pretends to have just crude data not processed data, in order to replacate all the ETLs that are necessary to deploy a model 
    * The sql_table_parser relies complitly on sqlparse library https://pypi.org/project/sqlparse/ 
          * the documentation is in here https://buildmedia.readthedocs.org/media/pdf/sqlparse/latest/sqlparse.pdf 
