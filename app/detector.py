def detect_incident(error_rate):
    if error_rate >= 0.25:
        incident_type = "HIGH_ERROR_RATE"
        recommendation = "Inspect application errors and relevant logs."
    elif error_rate >= 0.10:
        incident_type = "ELEVATED_ERROR_RATE"
        recommendation = "Monitor the service and investigate the error increase."
    else:
        incident_type = "LOW_ERROR_RATE"
        recommendation = "No immediate action required."
    return incident_type, recommendation