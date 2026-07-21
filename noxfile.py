import nox

PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13", "3.14"]


@nox.session(python=PYTHON_VERSIONS, venv_backend="uv")
def tests(session: nox.Session) -> None:
    """Run the test suite."""
    session.install(".", "pytest", "pexpect")
    session.run("pytest", *session.posargs)
