# import django
from django.core.management.utils import get_random_secret_key

# Generate a new secret key
print(get_random_secret_key())
