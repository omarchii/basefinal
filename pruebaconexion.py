import psycopg2
from psycopg2 import OperationalError

def test_postgresql_connection():
    try:
        # Conexión
        connection = psycopg2.connect(
            host="localhost",       # Cambia según tu configuración
            database="appdb",  # Nombre de tu base de datos
            user="app_user",      # Usuario PostgreSQL
            password="1234",  # Contraseña PostgreSQL
            port=5432  # Puerto por defecto de PostgreSQL
        )
        # Confirmar la conexión
        print("Conexión exitosa a PostgreSQL")

        # Obtener información del servidor
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Versión de PostgreSQL: {db_version}")

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()
        print("Conexión cerrada")
    except OperationalError as e:
        print(f"Error al conectar a PostgreSQL: {e}")

# Llamar la función
test_postgresql_connection()