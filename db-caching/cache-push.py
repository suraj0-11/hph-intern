import redis
import psycopg2
from sshtunnel import SSHTunnelForwarder

# SSH and Database configuration
SSH_HOST = #add your host in string
SSH_USER = #add user in string
SSH_PASSWORD = #password
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = 5544
POSTGRES_USER = #user of db
POSTGRES_PASSWORD = #password of db
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None

# Dummy data for PostgreSQL
dummy_data = [
    ("John Doe", 30),
    ("Jane Smith", 25),
    ("Alice Brown", 28)
]

def setup_database_and_cache():
    try:
        # Step 1: Establish SSH tunnel
        with SSHTunnelForwarder(
            (SSH_HOST, 22),
            ssh_username=SSH_USER,
            ssh_password=SSH_PASSWORD,
            remote_bind_address=('localhost', POSTGRES_PORT),
            local_bind_address=('localhost', 5555)
        ) as tunnel:
            print("SSH tunnel established.")
            
            # Step 2: Connect to PostgreSQL
            pg_conn = psycopg2.connect(
                host='localhost',
                port=tunnel.local_bind_port,
                user=POSTGRES_USER,
                password=POSTGRES_PASSWORD,
                dbname='gathjod'
            )
            cursor = pg_conn.cursor()

            # Drop existing table if needed (comment out if you don't want to reset the table)
            cursor.execute("DROP TABLE IF EXISTS suraj;")
            pg_conn.commit()
            
            # Create table with correct schema
            cursor.execute("""
                CREATE TABLE suraj (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    age INTEGER
                );
            """)
            pg_conn.commit()
            print("Table 'suraj' created successfully.")

            # Insert dummy data with explicit columns
            for name, age in dummy_data:
                cursor.execute(
                    "INSERT INTO suraj (name, age) VALUES (%s, %s);",
                    (name, age)
                )
            pg_conn.commit()
            print("Dummy data inserted into 'suraj' table.")

            # Step 3: Connect to Redis
            r = redis.StrictRedis(
                host=REDIS_HOST,
                port=REDIS_PORT,
                password=REDIS_PASSWORD,
                decode_responses=True
            )

            # Step 4: Cache data from PostgreSQL in Redis
            cursor.execute("SELECT * FROM suraj;")
            rows = cursor.fetchall()
            for row in rows:
                user_id, name, age = row
                r.hset(f"user:{user_id}", mapping={
                    "name": name,
                    "age": str(age)  # Convert to string for Redis storage
                })
            print("Data cached in Redis.")

            # Clean up
            cursor.close()
            pg_conn.close()
            print("Database connections closed.")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    setup_database_and_cache()
