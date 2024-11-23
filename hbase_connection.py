import happybase

class HBaseConnection:
    def __enter__(self):
        self.connection = happybase.Connection('localhost')
        print("Conexión establecida con HBase")
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
        print("Conexión cerrada con HBase")
