#---------------------------------------------------------------#
#  REMINDER: You need message.content intent for this to work.  #
#  Special thanks to:                                           #
#    Drizzly#9999                                               #
#    Arron#5192                                                 #
#---------------------------------------------------------------#

@client.command()
@commands.cooldown(1, 30, commands.BucketType.guild)
@commands.guild_only()
async def embed(ctx, channel: discord.TextChannel):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel 
    guide = await ctx.send("Welcome to the Embed Creation Tool. Follow the guide's steps to complete the creation of your embed.\nYou can generate a template embed to learn more about embeds with ``[prefix]template``\nIf you want to leave an element empty, type 0.\n**REMINDER: **Steps with an asterisk ('*') are required and cannot be left empty. Special arguments are case insensitive")
    
    await guide.reply('**STEP 1/8** - Insert title*:')
    title = await client.wait_for('message', check=check)

    await guide.reply('**STEP 2/8** - Insert description:')
    desc = await client.wait_for('message', check=check)

    await guide.reply('**STEP 3/8** - Insert color code*:\n\n**Available Colors:**\n1 - Red\n2 - Orange\n3 - Gold\n4 - Green\n5 - Teal\n6 - Blue\n7 - Pink\n8 - Purple\n9 - Cyan\n10 - Mint Green')
    color = await client.wait_for('message', check=check)
    
    await guide.reply('**STEP 4a/8** - Insert footer:')
    footer = await client.wait_for('message', check=check)
    if footer.content != '0' and footer.content != 'default':
        await guide.reply("**STEP 4b/8** - Do you want your footer to have an icon? Type:\n0 - No\nguild or server - To take the server's icon\nme - To take your icon")
        footer_icon = await client.wait_for('message', check=check)

    await guide.reply('**STEP 5a/8** - Insert author:')
    author = await client.wait_for('message', check=check)
    if author.content != '0':
        await guide.reply("**STEP 5b/8** - Do you want your author to have an icon? Type:\n0 - No\nguild or server - To take the server's icon\nme - To take your icon")
        author_icon = await client.wait_for('message', check=check)

    field_titles = []
    field_bodies = []
    await guide.reply('**STEP 6a/8** - Insert field title:')
    field_title = await client.wait_for('message', check=check)
    field_titles.append(field_title.content)
    while field_title.content != '0':
        await guide.reply('**STEP 6b/8** - Insert field body:')
        field_body = await client.wait_for('message', check=check)
        field_bodies.append(field_body.content)
        await guide.reply('**STEP 6a/8** - Insert field title:')
        field_title = await client.wait_for('message', check=check)
        field_titles.append(field_title.content)

    await guide.reply('**STEP 7/8** - Insert thumbnail:')
    thumbnail = await client.wait_for('message', check=check)
    
    await guide.reply('**STEP 8/8** - Insert image:')
    image = await client.wait_for('message', check=check)

    if color.content == "1":
        userEmbed = discord.Embed(title=title.content, description=desc.content, color=0xe74c3c)
    elif color.content == "2":
        userEmbed = discord.Embed(title=title.content, description=desc.content, color=0xe67e22)
    elif color.content == "3":
        userEmbed = discord.Embed(title=title.content, description=desc.content, color=0xf1c40f)
    elif color.content == "4":
        userEmbed = discord.Embed(title=title.content, description=desc.content, color=0x2ecc71)
    elif color.content == "5":
        userEmbed = discord.Embed(title=title.content, description=desc.content, color=0x1abc9c)
    elif color.content == "6":
        userEmbed = discord.Embed(title=title.content, description=desc.content, color=0x3498db)
    elif color.content == "7":
        userEmbed = discord.Embed(title=title.content, description=desc.content, color=0xe91e63)
    elif color.content == "8":
        userEmbed = discord.Embed(title=title.content, description=desc.content, color=0x9b59b6)
    elif color.content == "9":
        userEmbed = discord.Embed(title=title.content, description=desc.content, color=0x00ffff)
    elif color.content == "10":
        userEmbed = discord.Embed(title=title.content, description=desc.content, color=0x98ff98)    
    else: await ctx.send('**ERROR: **Invalid color code inserted. Please select a number from 1-10.')
        
    try:
        if field_titles[0] != '0':
            for i in range(len(field_bodies)):
                userEmbed.add_field(name=field_titles[i], value=field_bodies[i])
        
        if footer.content != '0': 
            if footer_icon.content == '0': userEmbed.set_footer(text=footer.content)
            elif footer_icon.content.lower() == 'me': userEmbed.set_footer(text=footer.content, icon_url=ctx.author.display_avatar)
            elif footer_icon.content.lower() == 'guild' or footer_icon.content == 'server': userEmbed.set_footer(text=footer.content, icon_url=ctx.guild.icon)
            else: await ctx.send('**ERROR: **Incorrect footer icon argument received. Please select between: ``0``, ``me``, ``guild/server``')
        
        if author.content != '0':
            if author_icon.content == '0': userEmbed.set_author(name=author.content)
            elif author_icon.content.lower() == 'me': userEmbed.set_author(name=author.content, icon_url=ctx.author.display_avatar)
            elif author_icon.content.lower() == 'guild' or author_icon.content == 'server': userEmbed.set_author(name=author.content, url=ctx.guild.icon)
            else: await ctx.send('**ERROR: **Incorrect author icon argument received. Please select between: ``0``, ``me``, ``guild/server``')
        
        if thumbnail.attachments != [] and image.attachments != []:
            userEmbed.set_thumbnail(url=f'{thumbnail.attachments[-1].url}')
            userEmbed.set_image(url=f'{image.attachments[-1].url}')
            await channel.send(embed=userEmbed)
        elif thumbnail.attachments != [] and image.attachments == []:
            userEmbed.set_thumbnail(url=f'{thumbnail.attachments[-1].url}')
            await channel.send(embed=userEmbed)
        elif thumbnail.attachments == [] and image.attachments != []:
            userEmbed.set_image(url=f'{image.attachments[-1].url}')
            await channel.send(embed=userEmbed)
        else: await channel.send(embed=userEmbed)       
    except Exception as e:
        print(f'Embed Creator Exception: {e}')

@commands.command()
@commands.cooldown(1, 30, commands.BucketType.guild)
@commands.guild_only()
async def template(ctx):
    templateEmbed = discord.Embed(
        title='This the title',
        description='This the description. On the left you can see the color of the embed. In this case, it is red.',
        color = discord.Color.red()
    ).set_author(name='<- That is the author icon and this text is the author', icon_url=ctx.author.display_avatar)
    templateEmbed.add_field(name='This is the field title', value='This is the field body')
    templateEmbed.set_footer(text='<- This the footer icon and this text is the footer', icon_url=ctx.author.display_avatar)
    templateEmbed.set_thumbnail(url='https://media.discordapp.net/attachments/1011367580054859868/1011367733591556216/thumbnail.png').set_image(url='https://media.discordapp.net/attachments/1011367580054859868/1011367708262154250/image.png')
    await ctx.send(embed=templateEmbed)
