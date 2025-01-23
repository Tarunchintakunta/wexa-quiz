from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from auth.models import User
from auth.schemas import UserCreate, UserLogin, Token
from auth.utils import hash_password, verify_password, create_access_token
from database import get_db
import logging

router = APIRouter()

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/signup", response_model=Token, status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        # Check if email already exists
        result = await db.execute(select(User).where(User.email == user.email))
        existing_user = result.scalars().first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Create new user
        hashed_password = hash_password(user.password)
        new_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password
        )
        db.add(new_user)
        await db.commit()

        logger.info(f"New user created: {user.email}")

        # Generate token
        access_token = create_access_token({"sub": new_user.email, "role": "user"})
        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        logger.error(f"Error during signup: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )


@router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    try:
        # Find user by email
        result = await db.execute(select(User).where(User.email == user.email))
        existing_user = result.scalars().first()
        if not existing_user or not verify_password(user.password, existing_user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        logger.info(f"User logged in: {user.email}")

        # Generate token
        access_token = create_access_token({"sub": existing_user.email, "role": "user"})
        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        logger.error(f"Error during login: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
