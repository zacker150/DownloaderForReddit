from DownloaderForReddit.database.DatabaseCreator import DatabaseCreator


"""
A tool used to create the required sqlite database from the command line.
"""

def main():
    db_creator = DatabaseCreator()
    db_creator.create_database()
    db_creator.close_connection()


if __name__ == '__main__':
    main()
    print('database created')
