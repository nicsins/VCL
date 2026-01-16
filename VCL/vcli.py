# vcl/cli.py
import click
from pathlib import Path
from .parser import transpile_vcl_to_python

@click.group()
def cli():
    """VCL - Vibe Coding Language CLI"""
    pass

@cli.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--output", "-o", default=None, help="Output Python file (default: same name .py)")
@click.option("--mode", "-m", default="dev", type=click.Choice(["dev", "prod"]),
              help="dev = keep hints/comments, prod = clean & optimized")
@click.option("--run", is_flag=True, help="Run the transpiled code immediately")
def transpile(file, output, mode, run):
    """Transpile a .vcl file to Python"""
    input_path = Path(file)
    if not input_path.suffix.lower() in [".vcl", ".dev.vcl"]:
        raise click.BadArgumentUsage("Input must be .vcl or .dev.vcl")

    try:
        python_code = transpile_vcl_to_python(input_path.read_text(), mode=mode)

        if output is None:
            output_path = input_path.with_suffix(".py")
        else:
            output_path = Path(output)

        output_path.write_text(python_code)
        click.echo(f"✨ Transpiled to {output_path}")

        if run:
            click.echo("\nRunning transpiled code...\n" + "="*50)
            exec(python_code, {"__file__": str(output_path)})  # careful in prod!

    except Exception as e:
        click.echo(f"💥 Transpile failed: {e}", err=True)
        # TODO: add friendly suggestions here later

if __name__ == "__main__":
    cli()
