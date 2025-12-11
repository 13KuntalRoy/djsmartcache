from django.conf import settings

REDIS_URL = getattr(settings, "SMARTCACHE_REDIS_URL", "redis://localhost:6379/0")
DEFAULT_TTL = getattr(settings, "SMARTCACHE_DEFAULT_TTL", 300)
USE_REDIS_LOCK = getattr(settings, "SMARTCACHE_USE_REDIS_LOCK", True)
LOCK_TIMEOUT = getattr(settings, "SMARTCACHE_LOCK_TIMEOUT", 5)
PUBSUB_CHANNEL = getattr(settings, "SMARTCACHE_PUBSUB_CHANNEL", "smartcache:updates")
START_LISTENER = getattr(settings, "SMARTCACHE_START_LISTENER", True)
JITTER_PCT = getattr(settings, "SMARTCACHE_JITTER_PCT", 0.1)  # 10% jitter by default
VALIDATE_SCHEMA = getattr(settings, "SMARTCACHE_VALIDATE_SCHEMA", False)
