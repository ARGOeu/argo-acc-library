#!/usr/bin/env python

from argparse import ArgumentParser
from argo_acc_library import ArgoAccountingService
import sys

if __name__ == "__main__":
    parser = ArgumentParser(description="Simple Argo Accounting metric fetch example")
    parser.add_argument(
        "--host",
        type=str,
        default="api.devel.acc.argo.grnet.gr",
        help="FQDN of Argo Accounting Service",
    )
    parser.add_argument(
        "--token", type=str, required=True, help="JWT authentication token"
    )
    parser.add_argument(
        "-f",
        help="treat the JWT authentication token argument as a path to a file holding the token",
        action="store_true",
    )
    args = parser.parse_args()

    if args.f:
        try:
            with open(args.token, "r") as tokenfile:
                token = tokenfile.read()
        except Exception as e:
            print("Error while reading token from file:", str(e), file=sys.stderr)
            exit(1)
    else:
        token = args.token

    acc = ArgoAccountingService(args.host, token)
    try:
        for m in acc.installations:
            # print installation data as JSON string
            print(m)
    except Exception as e:
        print("Error while iterating installations:", str(e))
