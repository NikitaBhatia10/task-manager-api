from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User, Task
from schemas import UserCreate, UserResponse, TaskCreate, TaskResponse
from auth import get_password_hash, verify_password, create_access_token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBearer, HTTPAuthorizationCredentials
from fastapi.security import OAuth2PasswordBearer
from jwt_handler import verify_access_token
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuthFlowPassword
from fastapi.security import OAuth2
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

Base.metadata.create_all(bind=engine)
app = FastAPI()
security = HTTPBearer()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------
# USER AUTH ROUTES
# -------------------

@app.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    if not isinstance(user.password, str) or len(user.password) > 72:
        raise HTTPException(status_code=400, detail="Password must be a string under 72 characters")
    print("DEBUG:", type(user.password), user.password)
    print("DEBUG password type:", type(user.password))
    print("DEBUG password value:", user.password)

    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing"
        )
    token = credentials.credentials
    payload = verify_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    username = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )
    return username

@app.get("/tasks/protected")
def read_protected_tasks(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello {current_user}, here are your protected tasks!"}
