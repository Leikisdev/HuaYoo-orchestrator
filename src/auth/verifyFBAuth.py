import os
import firebase_admin
from firebase_admin import auth

class VerifyFBAuth:
    def __init__(self):
        # Only initialize once
        if not firebase_admin._apps:
            firebase_admin.initialize_app()

    def verify_token(self, token: str):
        try:
            decoded_token = auth.verify_id_token(token)
            return decoded_token
        except Exception as e:
            print(e)
            return None
        
