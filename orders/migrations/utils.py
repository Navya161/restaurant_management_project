import string
import random
from django.utils.crypto
import get_random_string
def generate_unique_coupon code(model,field="code",
length=10);
chars =string.ascii_uppercase+string.digits
while True:
    code =get_random_string(length = length ,allowed_char =chars)
    if not model.objects.filter(**{field:code}).exits():
        return code