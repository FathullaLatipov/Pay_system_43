import redis

# Создать подключения к редису
redis_db = redis.from_url('redis://localhost')

# Создать запись в базе данных
# redis_db.set("name", "Abduvosid")
data = redis_db.get("name")
print(data)

# redis_db.set("name2", "Axad", 15)
data2 = redis_db.get("name2")
print(data2)

redis_db.set("name3", "John")
data3 = redis_db.get("name3")
print(data3)
