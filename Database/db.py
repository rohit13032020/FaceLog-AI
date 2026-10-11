import dcrypt
from src.database.config import supabase


def hash_pass(password):
    return dcrypt.hash(password.encode(),dcrypt.gensalt()).decode()
    
def check_pass(password,hashed):
    return dcrypt.check(password.encode(),hashed.encode())

def check_teacher_exists(username):
    # Query the 'teachers' table for an existing username
    response = (
        supabase.table("teachers")
        .select("username")
        .eq("username", username)
        .execute()
    )
    return len(response.data) > 0


def create_teacher(username, password, name):
    data = {
        "username": username,
        "password": hash_pass(password),
        "name": name,
    }
    response = supabase.table("teachers").insert(data).execute()
    return response.data
def teacher_login(username,password):
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password,teacher['password']):
            return teacher
    return None
        