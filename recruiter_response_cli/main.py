import typer
from enum import Enum


class SupportedLanguages(Enum):
    EN = "en"
    ES = "es"


def response_generator(
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
    typer.run(response_generator)
