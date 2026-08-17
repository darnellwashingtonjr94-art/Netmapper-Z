from fastapi import APIRouter, HTTPException
from api.schemas import ScanRequest
from core.engine import run_scan

router = APIRouter()

@router.post("/scan")
def trigger_scan(payload: ScanRequest):
    try:
        # Trigger core engine execution
        run_scan(payload.target, payload.mode, payload.ports, "api_report.json")
        return {"message": "Scan executed successfully", "target": payload.target}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
