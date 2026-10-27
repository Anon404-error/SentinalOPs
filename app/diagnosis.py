
def diagnose_issues(main_logs):
    if main_logs["database"] > 0 and main_logs["network"] > 0:
        return "Both database and network issues detected."
    elif main_logs["database"] > 0:
        return "Database issues detected."
    elif main_logs["network"] > 0:
        return "Network issues detected."
    else:
        return "No issues detected."
    