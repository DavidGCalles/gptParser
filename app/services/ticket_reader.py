import logging
import json
import requests


from config import Config


class TicketReader:
    """
    A class to handle ticket reading operations, including parsing images and
    cleaning API responses.

    Attributes:
    -----------
    headers : dict
        Headers required for making API requests, including authorization.

    response : dict or None
        Stores the API response after making a request.

    parse_result : str or None
        Stores the parsed result of a response string.

    Methods:
    --------
    clean_response(raw_string: str) -> str:
        Cleans the raw response string by extracting the relevant JSON content.

    parse_image(request_data: dict) -> dict:
        Parses an image from base64 encoded string using the specified model
        and returns the parsed result.

    Example:
    --------
    >>> reader = TicketReader()
    >>> request_data = {
    ...     "base64_image": "base64_encoded_string",
    ...     "model": "gpt-4o-mini",
    ...     "max_tokens": 900
    ... }
    >>> parsed_data = reader.parse_image(request_data)
    >>> print(parsed_data)
    {'parsed_key': 'parsed_value'}

    Note:
    -----
    Ensure that the 'base64_image' key is included in the request_data dictionary.
    """
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {Config.API_KEY}"
        }
        self.response = None
        self.analysis = None
        self.parse_result = None
    def clean_response(self, raw_string:str):
        """
        Cleans the raw response string by extracting the relevant JSON content.

        Parameters:
        raw_string (str): The raw string response to be cleaned.

        Returns:
        str: The cleaned response containing JSON data.
        """
        self.parse_result = raw_string.split("json",1)[-1].replace("```", "")
        return self.parse_result
    def parse_image(self, request_data:dict):
        """
        Parses an image from a base64 encoded string using the specified model
        and returns the parsed result.

        Parameters:
        request_data (dict): A dictionary containing request data including
                             the base64 encoded image, model, and max tokens.

        Returns:
        dict: The parsed result from the API response.

        Raises:
        KeyError: If 'base64_image' is not provided in request_data.
        """
        try:
            payload = {
                "model": request_data.get("model","gpt-4o-mini"),
                "messages": [
                    {
                    "role": "user",
                    "content": [
                        {
                        "type": "text",
                        "text": f"{Config.PARSER_PROMPT}"
                        },
                        {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{request_data['base64_image']}"
                        }
                        }
                    ]
                    }
                ],
                "max_tokens": request_data.get("max_tokens", 2000)
            }
        except KeyError as exc:
            logging.error("No se han proporcionado todos los datos necesarios en requestData")
            raise KeyError("No se ha proporcionado un base64 de la imagen") from exc
        self.response = requests.post("https://api.openai.com/v1/chat/completions",
                         headers=self.headers, json=payload, timeout=300).json()
        response_string = self.response["choices"][0]["message"]["content"]
        return json.loads(self.clean_response(response_string))
    def analyze_receipt(self, request_data:dict, receipt_object:dict):
        payload = {
            "model": request_data.get("model","gpt-4o-mini"),
            "messages": [
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": f"{Config.ANALYZER_PROMPT}"
                    },
                    {
                    "type": "text",
                    "text": f"{receipt_object}",
                    }
                ]
                }
            ],
            "max_tokens": request_data.get("max_tokens", 2000)
        }
        self.analysis = requests.post("https://api.openai.com/v1/chat/completions",
                         headers=self.headers, json=payload, timeout=300).json()
        response_string = self.analysis["choices"][0]["message"]["content"]
        print(response_string)
        return response_string
