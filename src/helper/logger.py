import datetime

class Logger:
    _quiet: bool = None

    @classmethod
    def log(cls, message: str, priority: bool=False, breaker:str|None=None) -> None:
        if cls._quiet and not priority:
            return

        if not breaker:
            breaker = ""
    
        print(f"{breaker} {datetime.datetime.now().strftime('%H:%M:%S.%f')} - {message}")