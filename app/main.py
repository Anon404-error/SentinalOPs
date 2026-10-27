from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated
from app.detector import detect_incident
from app.log_analyzer import analyze_logs
from app.diagnosis import diagnose_issues
from app.retriever import retrieve_documents

app = FastAPI()
class LogEntry(BaseModel):
    message: str

class IncidentInput(BaseModel):
    service_id: str
    error_rate : Annotated[float, Field(ge =0.0, le=1.0)]
    logs : list[LogEntry]

@app.get("/health")
def health_check():
    return {"status" : "Working"}

@app.post("/Incident")
def analyze_incident(incident : IncidentInput):
    service_id = incident.service_id
    error_rate = incident.error_rate
    incident_type, recommendation = detect_incident(error_rate)
    Logs = incident.logs
    log_counts = analyze_logs(Logs)
    diagnosis = diagnose_issues(log_counts)
    query_terms = []
    if log_counts["database"] > 0:
        query_terms.append("database")
    if log_counts["network"] > 0:
        query_terms.append("network")
    query = " ".join(query_terms)
    matched_documents = retrieve_documents(query)

    return {"service_id" : service_id,
            "error rate" : error_rate,
            "incident type" : incident_type,
            "recommendation" : recommendation,
            "Logs" : analyze_logs(Logs),
            "Diagnosis" : diagnosis}

