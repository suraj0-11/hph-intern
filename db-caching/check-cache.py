import redis

# Redis configuration
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None  # Use None if no password is set

# Connect to Redis
r = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True
)

# Retrieve and print all cached user data
user_keys = r.keys("user:*")
print("Cached data in Redis:")
for key in user_keys:
    user_data = r.hgetall(key)
    print(f"{key}: {user_data}")
