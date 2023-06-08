from typing import List

import aiofiles

from fastapi import UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import File, User
from schemas.files import FileInDB

async def upload_file_to_service(file: UploadFile, session: AsyncSession):
    async with aiofiles.open(file.filename, 'wb') as f:
            while contents := await file.read(1024 * 1024):
                await f.write(contents)


async def get_files_info(
          user: User,
          session: AsyncSession
) -> List[FileInDB]:
    stmt = select(File).where(File.user_id==User.id)
    results = await session.execute(stmt)
    return results
