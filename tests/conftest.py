def pytest_terminal_summary(terminalreporter, exitstatus):
    """Prints message after tests are complete."""
    if exitstatus == 0:  # All tests passed
        terminalreporter.write("\nAll tests have passed :)\n")
