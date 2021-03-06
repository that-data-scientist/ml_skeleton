from datetime import datetime
from typing import Any, Dict


def log_step(target_func: Any) -> Any:
    def log_step_console_out(*args: Dict, **kwargs: Dict) -> Any:
        start_time = datetime.now()
        print(
            """[Info] {timestamp} Executing {func_name}""".format(
                timestamp=start_time, func_name=target_func.__name__
            )
        )

        result = target_func(*args, **kwargs)

        end_time = datetime.now()
        print(
            """[Info] {timestamp} Done in {exec_time} seconds""".format(
                timestamp=end_time, exec_time=(end_time - start_time).seconds
            )
        )
        return result

    return log_step_console_out
