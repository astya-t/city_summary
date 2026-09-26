import requests
import time


def get_json(url, max_retries=3):
    last_error = None

    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            return response.json()

        except (
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError
        ) as error:
            last_error = error

        except requests.exceptions.HTTPError as error:
            status_code = error.response.status_code

            if status_code in (500, 502, 503, 504):
                last_error = error

            elif status_code == 429:
                retry_after = error.response.headers.get("Retry-After")

                if retry_after and retry_after.isdigit():
                    if attempt < max_retries - 1:
                        time.sleep(int(retry_after))
                        continue

                raise

            else:
                raise

        if attempt < max_retries - 1:
            time.sleep(1)

    raise last_error