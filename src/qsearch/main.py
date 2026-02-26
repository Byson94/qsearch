from qsearch.quiet_stderr import suppress_stderr
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from ddgs import DDGS
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Do some tiny quick searches."
    )

    parser.add_argument("query", metavar="<QUERY>", type=str, help="The string to search")

    parser.add_argument(
        "-n", "--max-results",
        type=int,
        default=1,
        help="Number of results (default: 1)"
    )

    parser.add_argument(
        "-r", "--region",
        default=None,
        help="Region code (default: None)"
    )

    parser.add_argument(
        "-s", "--safesearch",
        choices=["on", "moderate", "off"],
        default="moderate",
        help="Safe search level"
    )

    parser.add_argument(
        "-t", "--time",
        choices=["d", "w", "m", "y"],
        help="Time limit: day/week/month/year"
    )

    if len(sys.argv) == 1:
        parser.print_help()
        return 0

    args = parser.parse_args()

    search_kwargs = {
        "max_results": args.max_results,
        "safesearch": args.safesearch,
        "timelimit": args.time,
    }

    if args.region is not None:
        search_kwargs["region"] = args.region

    with suppress_stderr():
        with DDGS() as ddgs:
            results = list(ddgs.text(args.query, **search_kwargs))

    console = Console()

    for r in results:
        title = Text(r["title"], style="bold cyan")
        body = r["body"]
        console.print(Panel(body, title=title))


if __name__ == "__main__":
    sys.exit(main())