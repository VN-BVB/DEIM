import re
import importlib
from packaging.version import Version, InvalidVersion
from importlib.metadata import version, PackageNotFoundError

REQ_FILE = "requirements.txt"


def parse_requirements(path):
    reqs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            raw = line.strip()
            if not raw or raw.startswith("#"):
                continue

            # 去掉注释
            line = raw.split("#")[0].strip()

            # 匹配: name==x.y.z / name>=x.y.z / name
            m = re.match(r"([A-Za-z0-9_\-]+)\s*([<>=!]+)?\s*([\w\.]+)?", line)
            if not m:
                continue

            name, op, ver = m.groups()
            reqs.append((name, op, ver))
    return reqs


def check_package(name, op, req_ver):
    try:
        inst_ver = version(name)
    except PackageNotFoundError:
        return "MISS", None

    if not op or not req_ver:
        return "OK", inst_ver

    try:
        iv = Version(inst_ver)
        rv = Version(req_ver)
    except InvalidVersion:
        return "OK", inst_ver

    if op == "==":
        return ("OK", inst_ver) if iv == rv else ("WARN", inst_ver)
    elif op == ">=":
        return ("OK", inst_ver) if iv >= rv else ("WARN", inst_ver)
    elif op == "<=":
        return ("OK", inst_ver) if iv <= rv else ("WARN", inst_ver)
    elif op == ">":
        return ("OK", inst_ver) if iv > rv else ("WARN", inst_ver)
    elif op == "<":
        return ("OK", inst_ver) if iv < rv else ("WARN", inst_ver)

    return "OK", inst_ver


def main():
    reqs = parse_requirements(REQ_FILE)

    print(f"\nChecking environment against {REQ_FILE}\n")

    ok, miss, warn = 0, 0, 0

    for name, op, req_ver in reqs:
        status, inst_ver = check_package(name, op, req_ver)

        if status == "OK":
            ok += 1
            print(f"[ OK ]   {name} ({inst_ver})")
        elif status == "MISS":
            miss += 1
            print(f"[ MISS ] {name} (not installed)")
        elif status == "WARN":
            warn += 1
            print(
                f"[ WARN ] {name} "
                f"(installed={inst_ver}, required={op}{req_ver})"
            )

    print("\nSummary:")
    print(f"  OK   : {ok}")
    print(f"  WARN : {warn}")
    print(f"  MISS : {miss}")


if __name__ == "__main__":
    main()
