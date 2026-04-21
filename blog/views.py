import time
import asyncio
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World")


def sync_view(request):
    for i in range(1, 6):
        print(f"Contador síncrono: {i}")
        time.sleep(1)
    return HttpResponse("View síncrona concluída!")


async def _contar_em_background(n):
    for i in range(1, n + 1):
        print(f"Contador assíncrono: {i}")
        await asyncio.sleep(1)


async def async_view(request):
    asyncio.ensure_future(_contar_em_background(5))
    return HttpResponse("View assíncrona — resposta imediata enquanto a contagem ocorre em background!")
