import typer
from rich.table import Table
import yaml
import os

app = typer.Typer()
CONFIG_FILE_PATH = '~/.config/recruiter_response/config.yaml'

if not os.path.exists(os.path.dirname(CONFIG_FILE_PATH)):
    os.makedirs(os.path.dirname(CONFIG_FILE_PATH))

@app.command("set")
def set_response(
    key: str = typer.Option(help="Key to find the response snippet"),
    response: str = typer.Option(help="Content of the response for the recruiter"),
    language: str = typer.Option(help="Language in which to store the response")
):
    responses_by_lang = {}
    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH) as f:
            responses_by_lang = yaml.safe_load(f)

    if language not in responses_by_lang:
        responses_by_lang[language] = []

    responses_by_lang[language].append(
        {
            "key": key,
            "response": response
        }
    )
    with open(CONFIG_FILE_PATH, 'w') as f:
        yaml.dump(responses_by_lang, f)


@app.command("list")
def list_responses():
    responses_by_lang = {}
    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH) as f:
            responses_by_lang = yaml.safe_load(f)
    print(responses_by_lang)


@app.command("get")
def get_response(
        recruiter_name: str = typer.Option(help="Name of the recruiter to respond to"),
        lang: str = typer.Option(help="Language in which to return the response")
    ):
    print(f"Hello {recruiter_name}!")


def main():
    app()
