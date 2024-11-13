## Overview

This project demonstrates a simple caching solution using Python to manage data insertions into a PostgreSQL database and store the data in a Redis cache. The caching setup aims to improve database performance by storing frequently accessed data in Redis.

### Code Structure

1. **Database and SSH Setup** (`cache-push.py`):
   - The script establishes an SSH tunnel to securely connect to a remote PostgreSQL database.
   - It creates a table (`suraj`) in PostgreSQL and inserts sample data for testing.
   - The data is then cached in Redis, with each record stored as a hash for quick access.

2. **Redis Caching**:
   - The script fetches data from PostgreSQL and inserts it into Redis, using a `user:{id}` key structure.
   - Each user’s name and age are stored under their specific Redis hash key, enabling efficient retrieval.

3. **Retrieving Cached Data** (`check-cache.py`):
   - This script connects to Redis to retrieve and display all cached data.
   - It lists each `user` record stored in Redis, showing cached information without needing to query the database.
