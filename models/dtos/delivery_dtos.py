from pydantic import BaseModel


class DeliveryBase(BaseModel):
    class Config:
        from_attributes = True


class DeliveryResponse(DeliveryBase):
    package_name: str
    tracking_number: str
    delivery_provider: str
