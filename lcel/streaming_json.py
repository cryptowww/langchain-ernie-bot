#!/usr/bin/env python
# -*- coding: utf-8 -*-

# streaming_json.py

import sys
sys.path.append("..")
import settings

from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import asyncio


model = QianfanChatEndpoint(model = "ERNIE-Bot")
parser = JsonOutputParser()

# A function that operates on input streams.
async def _extract_country_names_streaming(input_stream):
    """A function that operates on input streams."""
    country_names_so_far = set()

    async for input in input_stream:
        if not isinstance(input, dict):
            continue

        if "countries" not in input:
            continue

        countries = input["countries"]

        if not isinstance(countries, list):
            continue

        for country in countries:
            name = country.get("name")
            if not name:
                continue
            if name not in country_names_so_far:
                yield name
                country_names_so_far.add(name)

chain = model | parser | _extract_country_names_streaming
#chain = model | parser

async def streamodel():
    async for s in chain.astream('output a list of the countries france, spain, india, china, russion, us and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`'):
        print(s, end="|", flush=True)
        #print(s, flush=True)

#if __name__ == "__main__":
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(streamodel())
#    loop.close()
asyncio.run(streamodel())
