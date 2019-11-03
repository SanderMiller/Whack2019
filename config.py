def connect_sql(instance, database = None):
    from google.storage.speckle.python.tool import google_sql    
    database = google_sql.DatabaseConfig(instance, database)

    sql_cmd_config = google_sql.config.SQLCmdConfig(None)
    sql_cmd_config.add('__googlesql__', instance, None, None, database,
                    google_sql.GoogleSqlDriver.NAME, None, None)
    sql_cmd = google_sql.GoogleSqlCmd(sql_cmd_config)
    sql_cmd.set_database(instance)

    sql_cmd.preloop()
    return sql_cmd._SQLCmd__db

connect_sql('whack2019','medrec')