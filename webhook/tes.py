from discord_webhook import DiscordWebhook, DiscordEmbed

url = "https://events.hookdeck.com/e/src_MDh3j5wkkyA7"

webhook = DiscordWebhook(url=url,username="jack",avatar_url="https://images.pexels.com/photos/267569/pexels-photo-267569.jpeg")

# create embed object for webhook
# you can set the color as a decimal (color=242424) or hex (color='03b2f8') number
embed = DiscordEmbed(title='Your Title', description='Lorem ipsum dolor sit', color='03b2f8')

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()