import typer
from rich import Table

app = typer.Typer()


@app.command("set")
def set_response(
    title: str = typer.Option(help="Title of the response snippet"),
    description: str = typer.Option(help="Content of the response for the recruiter"),
    language: str = typer.Option(help="Language in which to store the response")
):
    pass


@app.command("list")
def list_responses():
    pass


@app.command("get")
def get_response(
        recruiter_name: str = typer.Option(help="Name of the recruiter to respond to"),
        lang: str = typer.Option(help="Language in which to return the response")
    ):
    print(f"Hello {recruiter_name}!")


def main():
    app()
