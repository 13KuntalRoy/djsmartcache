
---

````markdown
# djsmartcache

A powerful distributed caching layer for Django, built on Redis.  
Provides auto-caching, auto-invalidation, dynamic cache keys, stampede protection, and distributed sync across multiple servers.

---

## 🚀 Installation

```bash
pip install djsmartcache
````

---

## ⚙️ Django Setup

### 1. Add to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...
    "djsmartcache",
]
```

### 2. Configure Redis

```python
SMARTCACHE_REDIS_URL = "redis://localhost:6379/0"
```

### 3. Optional Settings

```python
SMARTCACHE_DEFAULT_TTL = 300
SMARTCACHE_USE_REDIS_LOCK = True
SMARTCACHE_LOCK_TIMEOUT = 5
SMARTCACHE_PUBSUB_CHANNEL = "smartcache:updates"
SMARTCACHE_START_LISTENER = True
SMARTCACHE_JITTER_PCT = 0.1
SMARTCACHE_VALIDATE_SCHEMA = False
```

---

# 🧠 Features

| Feature                 | Description                                                     |
| ----------------------- | --------------------------------------------------------------- |
| **Auto caching**        | Decorator-based function caching with TTL                       |
| **Dynamic cache keys**  | Auto + custom key builders                                      |
| **Auto invalidation**   | Clears cache on model save/delete                               |
| **Stampede protection** | Redis locking prevents multiple recomputations                  |
| **Distributed sync**    | Multi-server cache invalidation via Redis Pub/Sub               |
| **Manual cache API**    | Fine control using `cache_get`, `cache_set`, `cache_invalidate` |

---

# 📌 Usage Examples

## 1. Basic Auto Caching

```python
from djsmartcache import smart_cached

@smart_cached(ttl=30)
def get_products():
    return Product.objects.all()
```

---

## 2. Dynamic Cache Keys

```python
@smart_cached(key="user:{user_id}:profile", ttl=60)
def get_profile(user_id):
    return User.objects.get(id=user_id)
```

Auto-key mode:

```python
@smart_cached()
def expensive_query(category):
    return Product.objects.filter(category=category)
```

---

## 3. Manual Cache Control

```python
from djsmartcache import cache_get, cache_set, cache_invalidate

cache_set("hello", "world", ttl=10)
value = cache_get("hello")        # → "world"
cache_invalidate("hello")
```

---

## 4. Auto Invalidation on Model Save/Delete

```python
product = Product.objects.get(id=1)
product.stock = 50
product.save()     # related cached keys auto-cleared
```

Works across all servers through Redis Pub/Sub.

---

## 5. Avoid Cache Stampede

Enabled by default with:

```python
SMARTCACHE_USE_REDIS_LOCK = True
```

Only one worker recomputes expensive functions; others wait.

---

# 🧪 Testing Locally

### Start Redis

```bash
docker run -p 6379:6379 redis
```

### Run Django server

```bash
python manage.py runserver
```

Call any cached view twice → second call is instant.

---

# 📁 Example Django View

```python
from djsmartcache import smart_cached
from django.http import JsonResponse

@smart_cached(ttl=20)
def demo(request):
    return JsonResponse({"value": "cached response"})
```

---

# 📄 License

MIT License

```

