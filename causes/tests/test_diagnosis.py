from app.diagnosis import diagnose_issues
from app.log_analyzer import analyze_logs

def test_analyze_logs(capsys):
    logs = [
        {"message": "Database connection failed"},
        {"message": "Network error occurred"},
        {"message": "Database error occurred"},
        {"message": "Network connection failed"}
    ]
    main_logs = analyze_logs(logs)

    captured = capsys.readouterr()
    assert "Database connection issue detected." in captured.out
    assert "Network error detected." in captured.out
    assert main_logs["database"] == 2
    assert main_logs["network"] == 2

def test_diagnose_issues():
    # Test case 1: Both database and network issues detected
    main_logs = {"database": 2, "network": 2}
    result = diagnose_issues(main_logs)
    assert result == "Both database and network issues detected."

    # Test case 2: Only database issues detected
    main_logs = {"database": 1, "network": 0}
    result = diagnose_issues(main_logs)
    assert result == "Database issues detected."

    # Test case 3: Only network issues detected
    main_logs = {"database": 0, "network": 2}
    result = diagnose_issues(main_logs)
    assert result == "Network issues detected."

    # Test case 4: No issues detected
    main_logs = {"database": 0, "network": 0}
    result = diagnose_issues(main_logs)
    assert result == "No issues detected."

def test_analyze_logs_and_diagnose_issues_integration(capsys):

    sample_logs = [
        {"message": "Database connection failed"},
        {"message": "Network error occurred"},
        {"message": "Database error occurred"},
        {"message": "Network connection failed"} 
    ]
    main_logs = analyze_logs(sample_logs)
    diagnosis = diagnose_issues(main_logs)
    assert diagnosis == "Both database and network issues detected."