from functools import reduce
import os
from pathlib import Path

def validate_reports():
    """Validates all reports from the report file"""
    reports = get_reports()

    valid_reports = 0
    for report in reports:
        if ((is_descending(report)[0] or is_ascending(report)[0]) and is_valid_difference(report)[0]):
            valid_reports += 1
    
    print(f"Total amount of valid reports is {valid_reports}")

def problem_dampener():
    """Validates all reports using the problem dampening method"""
    reports = get_reports()

    valid_reports = 0
    for report in reports:
        valid_asc, asc_idx = is_ascending(report)
        valid_desc, desc_idx = is_descending(report)
        valid_diff, diff_idx = is_valid_difference(report)

        if ((valid_asc or valid_desc) and valid_diff):
            valid_reports += 1
        elif (recheck_report(report, asc_idx, desc_idx, diff_idx)):
            valid_reports += 1
   
    print(f"Total amount of valid dampened reports is {valid_reports}")

def get_reports() -> list[tuple]:
    """Gets all reports from the report file"""
    reports_file_path = Path(os.path.dirname(os.path.realpath(__file__))) / "reports.txt"
    reports: list[tuple] = []

    with open(reports_file_path, mode="r") as report_file:
        for report_line in report_file:
            reports.append(tuple(int(value) for value in report_line.split(" ")))

    return reports

def recheck_report(report: tuple, asc_idx: int, desc_idx: int, diff_idx: int) -> bool:
    """Rechecks if a report becomes valid if one number is taken out."""
    fault_idx = min(diff_idx, min([i for i in [asc_idx, desc_idx] if i > 0], default=0))
    for i in range(-1, 2):
        check_report = [report for idx, report in enumerate(list(report)) if idx != fault_idx + i]
        if (is_descending(check_report)[0] or is_ascending(check_report)[0]) and is_valid_difference(check_report)[0]:
            return True
        
    return False

def early_stop_reduce(function, iterable) -> tuple[bool, int]:
    """Uses a function to reduce a list, if function is not valid, stop early and return idx"""
    it = iter(iterable)
    value = next(it)
    for i, element in enumerate(it):
        if not function(value, element):
            return [False, i]
        value = element
    return [True, len(iterable)]

def is_descending(report: tuple) -> tuple[bool, int]:
    """Checks if all items in report are smaller than the last"""
    func = lambda a, b: a > b and b or False
    return early_stop_reduce(func, report)

def is_ascending(report: tuple) -> tuple[bool, int]:
    """Checks if all items in report are bigger than the last"""
    func = lambda a, b: a < b and b or False
    return early_stop_reduce(func, report)

def is_valid_difference(report: tuple):
    """Checks that the difference between all items and their follow up are between 1 and 3"""
    func = lambda a, b: 1 <= abs(a - b) <= 3 and b or False
    return early_stop_reduce(func, report)

validate_reports()
problem_dampener()