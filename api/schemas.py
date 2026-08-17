from pydantic import BaseModel, Field

class ScanRequest(BaseModel):
    target: str = Field(..., example="example.com")
    mode: str = Field("passive", example="active")
    ports: str = Field("top-100", example="22,80,443")
