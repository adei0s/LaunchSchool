class Banner:
    def __init__(self, message):
        self._message = message
        self._width = len(message) + 2

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return f"|{' '*self._width}|"

    def _horizontal_rule(self):
        return f"+{'-'*self._width}+"

    def _message_line(self):
        return f"| {self._message} |"
        
        
banner = Banner('To boldly go where no one has gone before.')
print(banner)