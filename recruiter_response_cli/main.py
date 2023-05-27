import typer
from enum import Enum

app = typer.Typer()

class SupportedLanguages(Enum):
    EN = "en"
    ES = "es"


@app.command("set")
def set_response():
    pass


@app.command("get")
def get_response(
        recruiter_name: str = typer.Option(help="Name of the recruiter to respond to"),
        lang: str = typer.Option(help="Language in which to return the response")
    ):
    if lang == SupportedLanguages.EN:
        print(f"Hello {recruiter_name}!")
    elif lang == SupportedLanguages.ES:
        print(f"¡Hola {recruiter_name}!")
    else:
        print("Language not supported!")


if __name__ == "__main__":
    app()
