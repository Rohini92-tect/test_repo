from app.Main import Main

def handler(event, context):
    print("event", event)
    data = Main.run(event, context)
    return data