import os
import asyncio
import zipfile
import tempfile
from telethon import events, types
from BANNED_FILES.config import ADS_CODES, POPPY_FOLDER

async def load_ads_command(client):
    async def delete_after_delay(message, delay=600):
        await asyncio.sleep(delay)
        try:
            await message.delete()
        except:
            pass

    async def send_with_autodelete(event, file_path, pin_code):
        filename = os.path.basename(file_path)
        msg = await client.send_file(
            event.chat_id,
            file_path,
            attributes=[types.DocumentAttributeFilename(filename)]
        )
        asyncio.create_task(delete_after_delay(msg))
        print(f"File #{pin_code} sent to chat {event.chat_id}")

    async def send_archive_with_autodelete(event, paths, pin_code):
        with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as tmp:
            temp_zip = tmp.name

        with zipfile.ZipFile(temp_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for path in paths:
                if os.path.isfile(path):
                    zipf.write(path, os.path.basename(path))
                elif os.path.isdir(path):
                    for root, _, files in os.walk(path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.join(os.path.basename(path),
                                                   os.path.relpath(file_path, path))
                            zipf.write(file_path, arcname)

        archive_name = f"BANNED_FILES.zip"
        msg = await client.send_file(
            event.chat_id,
            temp_zip,
            attributes=[types.DocumentAttributeFilename(archive_name)]
        )
        asyncio.create_task(delete_after_delay(msg))
        print(f"Archive #{pin_code} sent to chat {event.chat_id}")
        os.unlink(temp_zip)

    @client.on(events.NewMessage(pattern=r'(?i)^ads\s+(\d{4})$'))
    async def ads_handler(event):
        if not event.out:
            return

        pin_code = event.pattern_match.group(1)

        if pin_code not in ADS_CODES:
            return

        targets = ADS_CODES[pin_code]
        if isinstance(targets, str):
            targets = [targets]

        full_paths = [os.path.join(POPPY_FOLDER, target) for target in targets]
        if not all(os.path.exists(p) for p in full_paths):
            return

        if len(full_paths) == 1 and os.path.isfile(full_paths[0]):
            await send_with_autodelete(event, full_paths[0], pin_code)
        else:
            await send_archive_with_autodelete(event, full_paths, pin_code)

    @client.on(events.NewMessage(pattern=r'(?i)^ads$'))
    async def ads_help(event):
        if event.out:
            msg = await event.reply("Usage: ads <4-digit code>")
            asyncio.create_task(delete_after_delay(msg, 30))