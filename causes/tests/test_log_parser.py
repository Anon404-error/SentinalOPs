from app.log_analyzer import analyze_logs
def test_analyze_logs(capsys):
    logs = [
        {"message": "Database connection failed"},
        {"message": "Network error occurred"},
        {"message": "Database error occurred"},
        {"message": "Network connection failed"}
    ]
    result = analyze_logs(logs)

    captured = capsys.readouterr()
    assert "Database connection issue detected." in captured.out
    assert "Network error detected." in captured.out
    assert result["database"] == 2
    assert result["network"] == 2

def test_analyze_logs_no_issues(capsys):
    logs = [
        {"message": "All systems operational"},
    ]
    result = analyze_logs(logs)
    assert result == {"database": 0, "network": 0}

def test_analyze_logs_network_only(capsys):
    logs = [
        {"message": "Network error occurred"},
        {"message": "Network connection failed"}
    ]
    result = analyze_logs(logs)
    assert result == {"database": 0, "network": 2}

def test_analyze_logs_database_only(capsys):
    logs = [
        {"message": "Database connection failed"},
        {"message": "Database error occurred"}
    ]
    result = analyze_logs(logs)
    assert result == {"database": 2, "network": 0}

def test_analyze_logs_missing_message_key(capsys):
    logs = [
        {"status": "true connection failed"},
        {"msg": "no error occurred"}
    ]
    result = analyze_logs(logs)
    assert result == {"database": 0, "network": 0}

def test_analyze_logs_both_issues(capsys):
    logs = [
        {"message": "Database connection failed"},
        {"message": "Database and Network issues detected"}
    ]
    result = analyze_logs(logs)
    assert result == {"database": 2, "network": 1}