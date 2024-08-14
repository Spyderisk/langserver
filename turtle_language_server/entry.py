from turtle_language_server.server import ttl_server
from sys import argv

def main():
    if argv[1] in ["--tcp"]:
        ip, port = argv[2].split(':')
        ttl_server.start_tcp(ip, port)
    else:
        ttl_server.start_io()


if __name__ == "__main__":
    main()

