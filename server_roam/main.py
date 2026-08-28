from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def health():
    return {"status": "running"}

@app.post("/webhooks/roam")
async def roam_webhook(request: Request):
    body = await request.json()

    if body.get("type") != "chat.message":
        return {"ok": True}

    data = body.get("data", {})

    # Prevent processing messages sent by our own bot
    if data.get("userType") == "bot":
        return {"ok": True}

    message = {
        "text": data.get("text"),
        "user_id": data.get("userId"),
        "chat_id": data.get("chatId"),
        "chat_type": data.get("chatType"),
    }

    print("\n=== ROAM MESSAGE ===")
    print(message)
    print("====================\n")

    return {"ok": True}