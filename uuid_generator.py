import uuid

# Create UUID function
def generate_uuid():
    return str(uuid.uuid4())

print("UUID:", generate_uuid())