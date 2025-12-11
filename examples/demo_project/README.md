A simple demo showing how to integrate django-smartcache in a Django project.
1. Add `djsmartcache` to INSTALLED_APPS
2. Configure SMARTCACHE_REDIS_URL in settings
3. Start Redis locally
4. Run server and observe cache invalidation when saving models.
