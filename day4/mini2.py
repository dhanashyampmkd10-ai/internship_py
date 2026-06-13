class HTTPError(Exception):
    def __init__(self, status_code: int, message: str = ""):
        self.status_code = status_code
        super().__init__(message)
def get_or_404(collection: dict, id: int) -> dict:
    if id in collection:
        return collection[id]
    raise HTTPError(404, "Item not found")
items = {}
items[1] = {"id": 1, "name": "DHANASHAYAM"}
items[2] = {"id": 2, "name": "AYAS"}
items[3] =   {"id": 3, "name": "ABER"}
print(get_or_404(items, 1))
try:
    print(get_or_404(items, 99))
except HTTPError as e:
    print(f"Error {e.status_code}: {e}")