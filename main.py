import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--echo", help = "help message")
# parser.add_argument("hello", help = "hello message")
# args = parser.parse_args()
# print(args.echo)
# print(args.hello)

# parser = argparse.ArgumentParser()
# parser.add_argument("--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# print(args.verbose)
# if args.verbose:
#     print("verbosity turned on")

parser = argparse.ArgumentParser()
parser.add_argument("--source_folder", help = "pls enter --s and than name of source folder", action="store")
parser.add_argument("--replica_folder", help = "pls enter --r and than name of replica folder", action="store")
parser.add_argument("--interval", help = "pls enter --i and than interval time(in second)", type=int, action="store")
args = parser.parse_args()
source_folder = args.source_folder
replica_folder = args.replica_folder
interval = args.interval
print(replica_folder, source_folder, interval)