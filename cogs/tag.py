from enum import Enum
from typing import TypedDict

import discord
from discord import app_commands
from discord.ext import commands

from utils.commands import HexBugBot


class Tag(TypedDict, total=False):
    content: str
    embed: discord.Embed


class Tags(Enum):
    crashlog = Tag(
        embed=discord.Embed(
            description="""You can use a service like [Pastebin](https://pastebin.com) to post the crashlog.
Do ***NOT*** upload it directly to Discord in a message or file."""
        ).set_image(url="https://cdn.discordapp.com/attachments/326397739074060288/976135876046356560/image0-4-2.gif"),
    )

    git_log = Tag(content="https://xkcd.com/1296/")

    bug_report = Tag(
        embed=discord.Embed(
            description="""Please do not post your bug reports to Discord. Instead, post them to the issue tracker on the mod's Github.

Hexcasting: https://github.com/gamma-delta/HexMod/issues
PAUCAL: https://github.com/gamma-delta/PAUCAL/issues""",
        ),
    )

    pk = Tag(
        embed=discord.Embed(
            description="""**What are all the `[BOT]` messages doing?**
This is the result of PluralKit, a discord bot for plural people. Plurality is the experience of having more than one mind in one body.

PluralKit info: https://pluralkit.me/
More info on plurality: https://morethanone.info/""",
        ),
    )


class TagCog(commands.Cog):
    def __init__(self, bot: HexBugBot) -> None:
        self.bot = bot

    @app_commands.command()
    @app_commands.describe(
        tag="The name of the tag to show",
    )
    @app_commands.rename(tag="name")
    async def tag(self, interaction: discord.Interaction, tag: Tags):
        """Show a premade info message"""
        value: Tag = tag.value
        await interaction.response.send_message(**value)


async def setup(bot: HexBugBot) -> None:
    await bot.add_cog(TagCog(bot))