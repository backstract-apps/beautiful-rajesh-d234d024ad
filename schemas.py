from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class Users(BaseModel):
    name: Optional[str]=None
    email: Optional[str]=None
    password: Optional[str]=None
    mobile: Optional[Union[int, float]]=None


class ReadUsers(BaseModel):
    name: Optional[str]=None
    email: Optional[str]=None
    password: Optional[str]=None
    mobile: Optional[Union[int, float]]=None
    class Config:
        from_attributes = True


class Students(BaseModel):
    pass


class ReadStudents(BaseModel):
    class Config:
        from_attributes = True


class MaysonRequestLogger(BaseModel):
    ts_utc: Optional[datetime.time]=None
    method: Optional[str]=None
    path: Optional[str]=None
    status_code: Optional[Union[int, float]]=None
    duration_ms: Optional[float]=None
    client_ip: Optional[str]=None
    user_agent: Optional[str]=None
    content_length: Optional[Union[int, float]]=None
    style: Optional[str]=None
    message: Optional[str]=None
    query_params: Optional[str]=None


class ReadMaysonRequestLogger(BaseModel):
    ts_utc: Optional[datetime.time]=None
    method: Optional[str]=None
    path: Optional[str]=None
    status_code: Optional[Union[int, float]]=None
    duration_ms: Optional[float]=None
    client_ip: Optional[str]=None
    user_agent: Optional[str]=None
    content_length: Optional[Union[int, float]]=None
    style: Optional[str]=None
    message: Optional[str]=None
    query_params: Optional[str]=None
    class Config:
        from_attributes = True


class Products(BaseModel):
    name: Optional[str]=None
    price: Optional[str]=None


class ReadProducts(BaseModel):
    name: Optional[str]=None
    price: Optional[str]=None
    class Config:
        from_attributes = True


class ItemsSold(BaseModel):
    quantity: Optional[Union[int, float]]=None
    price_per_item: Optional[Union[int, float]]=None
    price: Optional[float]=None


class ReadItemsSold(BaseModel):
    quantity: Optional[Union[int, float]]=None
    price_per_item: Optional[Union[int, float]]=None
    price: Optional[float]=None
    class Config:
        from_attributes = True


