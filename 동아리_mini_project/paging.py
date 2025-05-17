import json
from typing import List, Any

class Paginator:
    def __init__(self, data: List[Any], page_size: int):
        self.data = data
        self.page_size = page_size
        self.total_pages = (len(data) + page_size - 1) // page_size

    def get_page(self, page_number: int) -> List[Any]:
        if page_number < 1 or page_number > self.total_pages:
            return []
        start = (page_number - 1) * self.page_size
        end = start + self.page_size
        return self.data[start:end]

    @staticmethod
    def from_json_file(file_path: str, page_size: int):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return Paginator(data, page_size)

# Example usage:
if __name__ == "__main__":
    # Suppose 'data.json' contains a JSON array, e.g. [1,2,3,4,5,6,7,8,9,10]
    paginator = Paginator.from_json_file('data.json', page_size=3)
    for page in range(1, paginator.total_pages + 1):
        print(f"Page {page}: {paginator.get_page(page)}")