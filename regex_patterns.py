# regex_patterns.py (hosted on GitHub)
import re

def get_red_regex_patterns():
    return {
        "re_pattern1": re.compile(r'^(\d+)\s+(\d{14})\s+(\d+)\s+(\d+)\s+'),
        "re_pattern2": re.compile(r'^(\d{14})\s+(\d+)\s+(\d+)'),
        "re_pattern3": re.compile(r'^(\d{2}/\d{2}/\d{2})\s+(\d{2}:\d{2})\s+(\d+)\s+(\d+)'),
        "re_pattern4": re.compile(r'^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2})\s+(\d+)\s+(\d+)'),
        "re_pattern5": re.compile(r'^(\d+)\s+(\d{2}/\d{2}/\d{2})\s+(\d{2}:\d{2})\s+(\d+)\s+(\d+)')
    }
