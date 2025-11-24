import psycopg2


def check_tables():
    try:
        conn = psycopg2.connect(
            host="40.233.21.255",
            port=5432,
            database="autopartes",
            user="postgres",
            password="samipro"
        )
        cursor = conn.cursor()

        # Verificar si existen las tablas
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            AND table_name IN ('ventas', 'detalle_venta')
        """)

        tables = cursor.fetchall()
        print("Tablas encontradas:", tables)

        # Ver estructura de ventas si existe
        cursor.execute("""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = 'ventas'
        """)
        print("Columnas de ventas:", cursor.fetchall())

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    check_tables()# Este es un codigo para que, al ejecutarlo, nos diga los datos de las tablas que usa esta API en la base de datos
