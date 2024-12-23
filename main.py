import sys
import time
from src.fetcher import check_access, fetch_messages
from src.processer import process_messages
from src.plotter import plot_messages
from src.helper.logger import Logger

def help() -> None:
    print("""**Help**
Flags
-q Enables quiet mode and suppresses most messages
-h Displays this help page
-v Displays the current version
          
Options
--channel=<id> Fetches messages from the given channel without asking the user.
--token=<token> Will use the given token without asking the user.
--requests-count=<int> Amount of requests that may be send. This is an inclusive upper bound. Leave empty for unlimited.
--request-size=<int> Amount of messages you want to get per request. Defaults to 50.
""")

def version() -> None:
    print("0.1.0")

def fetch_and_analyse(channel_id: str, token: str, max_requests: int, _requests_size: int) -> None:
    access = check_access(channel_id, token)

    if not access:
        token = "Bot " + token
        access = check_access(channel_id, token)
    if not access:
        print("You do not have access to that channel or it does not exist.")
        return

    messages = fetch_messages(channel_id, token, max_requests, _requests_size)
    messages = process_messages(messages)
    plot_messages(messages)

def main(args: list[str]) -> None:
    _quiet = "-q" in args
    _help = "-h" in args
    _version = "-v" in args
    _channel = None
    _token = None
    _request_count = None
    _requests_size = None

    for arg in args:
        if arg.startswith("--channel="):
            _channel = arg.removeprefix("--channel=")
        if arg.startswith("--token="):
            _token = arg.removeprefix("--token=")
        if arg.startswith("--requests-count="):
            _request_count = int(arg.removeprefix("--requests-count="))
        if arg.startswith("--request-size="):
            _requests_size = int(arg.removeprefix("--request-size="))

    if _help: 
        help()
        return
    if _version:
        version()
        return

    Logger._quiet = _quiet

    if not _channel:
        _channel = input("Channel to analyse: ")
    if not _token:
        _token = input("Your Discord token: ")
    if not _request_count or _request_count <= 0:
        _request_count = -1
    if not _requests_size or _requests_size > 50 or _requests_size <= 0:
        _requests_size = 50

    fetch_and_analyse(_channel, _token, _request_count, _requests_size)

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
    time.sleep(5)