from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from .garage import api_keys


def api_key_auth(api_key: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    if api_key not in api_keys.values():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)