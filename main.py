import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, text
from faker import Faker

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

def main():
# 1. Conexión inicial al servidor MySQL (sin especificar la base de datos) para crearla si no existe
    base_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"
    temp_engine = create_engine(base_url)
    
    with temp_engine.begin() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`;"))
    print(f"Base de datos '{DB_NAME}' verificada o creada exitosamente.")

    # 2. Conexión oficial a la base de datos ya creada
    DATABASE_URL = f"{base_url}/{DB_NAME}"
    engine = create_engine(DATABASE_URL)
    
    metadata = MetaData()
    
    # 2. Definición de la tabla
    tabla_personas = Table(
        "Personas_Jimmy", 
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("nombre", String(100)),
        Column("correo", String(120)),
        Column("fecha_nacimiento", Date()),
        Column("ciudad", String(100)),
        Column("telefono", String(30)),
        Column("ocupacion", String(100)),
        Column("compania", String(100))
    )
    
    # Crear la tabla automáticamente si no existe
    metadata.create_all(engine)
    print("Tabla creada exitosamente (o ya existía).")
    
    # 3. Generación de datos con Faker
    fake = Faker('es_CO') # Configurado en español
    print("Generando 100,000 registros...")
    
    registros = []
    for _ in range(100000):
        registros.append({
            "nombre": fake.name(),
            "correo": fake.email(),
            "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=80),
            "ciudad": fake.city(),
            "telefono": fake.phone_number()[:30],
            "ocupacion": fake.job()[:100],
            "compania": fake.company()[:100]
        })
        
    # 4. Inserción masiva optimizada por lotes
    print("Insertando registros en la base de datos")
    with engine.begin() as conn:
        batch_size = 5000
        for i in range(0, len(registros), batch_size):
            conn.execute(tabla_personas.insert(), registros[i:i+batch_size])
            
    print("¡100,000 registros insertados con éxito!")
    
if __name__ == "__main__":
    main()