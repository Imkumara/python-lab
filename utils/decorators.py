import functools

def require_auth(func):
    @functools.wraps(func)
    def wrapper(session_user, *args, **kwargs):
        if not session_user:
            print("Access Denied: Authentication required. Please log in.")
            return None
        return func(session_user, *args, **kwargs)
    return wrapper

def require_admin(func):
    @functools.wraps(func)
    def wrapper(session_user, *args, **kwargs):
        if not session_user or session_user.role != "Admin":
            print("Access Denied: Admin privileges required.")
            return None
        return func(session_user, *args, **kwargs)
    return wrapper