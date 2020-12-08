#!/usr/bin/python3

import click


@click.group()
# @click.option('--debug/--no-debug', default=False)
@click.option('--count', default=1, help='Number of greetings.')
@click.pass_context
def cli(ctx, count):
    ctx.ensure_object(dict)
    # ctx.obj['DEBUG'] = debug
    ctx.obj['COUNT'] = count



@cli.command(name='gen')
@click.pass_context
@click.option('--deb/--no-deb', default=False)
def generic(ctx, deb):
    click.echo('Hello there: %s' % ctx.obj["COUNT"])
    click.echo('Hello there: %s' % deb)


@cli.command(name='wel')
@click.pass_context
def welcome(ctx):
    click.echo('Welcome')


# if __name__ == '__main__':
#     # cli(obj={})
#     cli()

if __name__ == '__main__':
    cli()