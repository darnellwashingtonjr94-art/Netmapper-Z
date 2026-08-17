from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.logger import get_logger

logger = get_logger()

def run_concurrent_tasks(task_func, items, max_workers=5):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_item = {executor.submit(task_func, item): item for item in items}
        for future in as_completed(future_to_item):
            item = future_to_item[future]
            try:
                data = future.result()
                results.append(data)
            except Exception as e:
                logger.error(f"Task failed for {item}: {e}")
    return results
