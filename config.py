#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from dotenv import load_dotenv

class DefaultConfig:
    """ Bot Configuration """
    load_dotenv()

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "3c699fe5-4776-47a0-93ca-baa0258c7958")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "sjD8Q~pzxGQ3FQHil2TLW9Fg6Gsg.zRW2vA.Ydqs")
    #SETTINGS = BotFrameworkAdapterSettings("3c699fe5-4776-47a0-93ca-baa0258c7958", "sjD8Q~pzxGQ3FQHil2TLW9Fg6Gsg.zRW2vA.Ydqs")

