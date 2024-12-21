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
--channel=<id> Fetches messages from the given channel without asking the user
--token=<token> Will use the given token without asking the user
""")

def version() -> None:
    print("0.1.0")

def fetch_and_analyse(channel_id: str, token: str) -> None:
    access = check_access(channel_id, token)

    if not access:
        token = "Bot " + token
        access = check_access(channel_id, token)
    if not access:
        print("You do not have access to that channel or it does not exist.")
        return

    messages = fetch_messages(channel_id, token)
    messages = process_messages(messages)
    plot_messages(messages)

def main(args: list[str]) -> None:
    _quiet = "-q" in args
    _help = "-h" in args
    _version = "-v" in args
    _channel = None
    _token = None

    for arg in args:
        if arg.startswith("--channel="):
            _channel = arg.removeprefix("--channel=")
        if arg.startswith("--token="):
            _token = arg.removeprefix("--token=")

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

    fetch_and_analyse(_channel, _token)

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
    time.sleep(5)