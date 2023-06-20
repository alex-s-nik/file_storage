from typing import List

import aiofiles

from aiopath import AsyncPath
from fastapi import HTTPException, status, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import UPLOAD_DIR
from models import File, User
from schemas.files import FileCreate, FileInDB


async def upload_file_to_service(path: str, file: UploadFile, user: User, session: AsyncSession):
    path = path.strip('/').strip('\\')
    abs_path = AsyncPath(UPLOAD_DIR, str(user.id), path)
    full_filename = AsyncPath(abs_path, file.filename)
    if not await abs_path.exists():
        await abs_path.mkdir(parents=True, exist_ok=True)

    async with aiofiles.open(full_filename, 'wb') as f:
        while contents := await file.read(1024 * 1024):
            await f.write(contents)
    # mark about this action in db
    uploaded_file_record: dict = FileCreate(
        name=file.filename,
        path=path,
        size=file.size,
        user_id=user.id
    ).dict()

    db_record = File(**uploaded_file_record)
    session.add(db_record)
    await session.commit()


async def get_files_info(
        user: User,
        session: AsyncSession
) -> List[FileInDB]:
    stmt = select(File).where(File.user_id == User.id)
    results = await session.execute(stmt)
    return results


async def get_file_path_name(
    filepath: str,
    user: User,
    session: AsyncSession
) -> tuple[AsyncPath, str]:
    path = AsyncPath(UPLOAD_DIR, str(user.id), filepath)
    if not (await path.exists()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    filename = filepath.split('/')[-1]
    return path, filename
