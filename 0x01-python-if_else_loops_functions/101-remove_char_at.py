#!/usr/bin/python3
def remove_char_at(str, n):
    """Create string copy and remove character at position n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
