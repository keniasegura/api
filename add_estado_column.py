import psycopg2
def add_estado_column():
    try:
        conn = psycopg2.connect(
            host="40.233.21.255",
            port=5432,
            database="autopartes",
            user="postgres",
            password="samipro"
        )
        cursor = conn.cursor()

        # Agregar columna estado si no existe
        cursor.execute("""
            ALTER TABLE ventas 
            ADD COLUMN IF NOT EXISTS estado CHARACTER VARYING(50) DEFAULT 'pendiente'
        """)

        conn.commit()
        print("✅ Columna 'estado' agregada a la tabla ventas")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"❌ Error agregando columna: {e}")


if __name__ == "__main__":
    add_estado_column()