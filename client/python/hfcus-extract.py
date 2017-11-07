#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import time
import pyhfcus
from pyhfcus.rest import ApiException


import time
import datetime
import argparse


def main():
    """This is run if file is directly executed, but not if imported as
    module. Having this in a separate function  allows importing the file
    into interactive python, and still able to execute the
    function for testing"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url",
                        required=False,
                        default="http://hfcus.b12x.org:8080",
                        help="HFCuS URL",
                        type=str)

    parser.add_argument("-o", "--outfile",
                        required=False,
                        help="output file",
                        type=str)

    parser.add_argument("-s", "--submission",
                        required=False,
                        help="submission ids",
                        type=str)

    parser.add_argument("-v", "--verbose",
                        help="Option for running in verbose",
                        default=False,
                        type=bool)

    args = parser.parse_args()
    outfile = args.outfile
    url = args.url
    subid = args.submission
    client = pyhfcus.ApiClient(host=url)
    api_instance = pyhfcus.DefaultApi(api_client=client)

    if subid:
        submission = api_instance.hfc_submission_id_get(subid)
        print(submission)
    else:
        alldata = api_instance.hfc_get()
        print(alldata)

if __name__ == '__main__':
    """The following will be run if file is executed directly,
    but not if imported as a module"""
    main()


