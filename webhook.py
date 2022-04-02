from discord_webhook import DiscordWebhook, DiscordEmbed
import webhookconfig

for loadef in webhookconfig.loadhooks:
	print(f"Loading hook: {loadef}")
	activehook = getattr(webhookconfig, loadef)
	
	webhook = DiscordWebhook(url=activehook['hooks'], username=activehook['name'], content=activehook['content'])
	if activehook['embedrule'] == True:
		for activehookembed in activehook['embed']:
			embed = DiscordEmbed(title=activehookembed['name'], description=activehookembed['description'], color=activehookembed['color'])
			embed.set_author(name=activehookembed['author_name'], url=activehookembed['author_url'], icon_url=activehookembed['author_icon'])
			embed.set_image(url=activehookembed['image'])
			embed.set_thumbnail(url=activehookembed['thumbnail'])
			embed.set_footer(text=activehookembed['footer_name'], icon_url=activehookembed['footer_icon'])
			if activehookembed['timestamp'] == True:
				embed.set_timestamp()
			if activehookembed['fieldsrule'] == True:
				for activefield in activehookembed['fields']:
					embed.add_embed_field(name=activefield['name'], value=activefield['value'])
			webhook.add_embed(embed)
			print(f"Added Embed: {embed}")

	response = webhook.execute()