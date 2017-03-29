#!/usr/bin/python
import re

def get_testcase_summary(output):
    """! Searches output string

        String to find:
        [1459246276.95][CONN][INF] found KV pair in stream: {{__testcase_summary;7;1}}, queued...

        @return Tuple of (passed, failed) or None if no summary found
    """
    print("Inside Test Summary")
    re_tc_summary = re.compile(r"^\[(\d+\.\d+)\][^\]+\{\{(__testcase_summary);(\d+);(\d+)\}\}")
    #re_tc_summary = re.compile(r"^\[(\d+\.\d+)\][^\{]+\{\{(__testcase_summary);(\d+);(\d+)\}\}")
    print("re_tc_summary =",re_tc_summary.pattern)
    #print(dir(re_tc_summary))
    
    for line in output.splitlines():
        print "line=",line
        m = re_tc_summary.search(line)
        print ("m=",m.groups())
        if m:
            _, _, passes, failures = m.groups()
            return int(passes), int(failures)
    return None


output = ("[1459246276.95][CONN][INF] found KV pair in stream: {{__testcase_summary;7;1}}, queued..")
get_testcase_summary(output)
