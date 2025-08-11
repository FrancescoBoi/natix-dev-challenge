from unittest.mock import patch
import pytest

@pytest.fixture
def mock_redis():
    # Define a fake Redis cache
    redis_cache = {}

    class MockRedis:
        def get(self, key):
            return redis_cache.get(key)

        def set(self, key, value):
            redis_cache[key] = value

    mock_instance = MockRedis()
    # PATCH THE REDIS USED IN app.routes (not app.__init__)
    with patch("app.routes.redis", mock_instance):
        yield mock_instance
