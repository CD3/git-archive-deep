"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Git Archive Deep."""


if __name__ == "__main__":
    main(prog_name="git-archive-deep")  # pragma: no cover
