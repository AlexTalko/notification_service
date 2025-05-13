import re
from typing import Union, List
from pydantic import BaseModel, Field, validator


# Pydantic-модель для валидации входящего запроса
class NotifyRequest(BaseModel):
    message: str = Field(..., max_length=1024)  # Текст сообщения, обязателен, макс. 1024 символа
    recipient: Union[str, List[str]]  # Получатель (строка или список строк)
    delay: int = Field(..., ge=0, le=2)  # Задержка (0, 1 или 2)

    @validator('recipient')
    def validate_recipient(cls, value):
        # Если получатель — строка, преобразуем в список
        if isinstance(value, str):
            value = [value]
        for recipient in value:
            # Проверка email по регулярному выражению
            if '@' in recipient:
                if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', recipient):
                    raise ValueError(f'Некорректный email: {recipient}')
            # Проверка Telegram ID (только цифры)
            else:
                if not recipient.isdigit():
                    raise ValueError(f'Некорректный Telegram ID: {recipient}')
        return value
