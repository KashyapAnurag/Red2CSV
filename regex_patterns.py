# regex_patterns.py
import re

def get_red_regex_patterns():
    return {
        "re_api": re.compile(r'^(\d+)\s+(\d{14})\s+(\d+)\s+(\d+)'),
        "re_radar": re.compile(r'^(\d{2}/\d{2}/\d{2})\s+(\d{2}:\d{2})\s+(\d+)\s+(\d+)'),
        "re_alt1": re.compile(r'^(\d{14})\s+(\d+)\s+(\d+)'),  # optional
        "re_alt2": re.compile(r'^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2})\s+(\d+)\s+(\d+)'),  # optional
    }
