import base64
import urllib.parse

class Core:

    def __init__(self):

        self.optionmenu_values = ["base64 - encode", "base64 - decode", "encodeURI", "decodeURI"]
        self.function_mapping = {"base64 - encode": self.base64_encode, "base64 - decode": self.base64_decode, "encodeURI": self.encodeURI, "decodeURI": self.decodeURI}

        return

    def base64_encode(self, input_string):
        clear_bytes = input_string.encode("ascii")

        base64_bytes = base64.b64encode(clear_bytes)
        encoded_string = base64_bytes.decode("ascii")
        return encoded_string

    def base64_decode(self, input_string):
        base64_bytes = input_string.encode("ascii")

        bytestring = base64.b64decode(base64_bytes)
        decoded_string = bytestring.decode("ascii")
        return decoded_string

    def encodeURI(self, input_string):
        return urllib.parse.quote_plus(input_string)

    def decodeURI(self, input_string):
        return urllib.parse.unquote_plus(input_string)
