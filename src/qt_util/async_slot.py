from threading import Thread


class AsyncSlot:
    def __init__(self, slot: callable) -> None:
        self._slot: callable = slot

    def __call__(self, *args, **kwargs) -> None:
        Thread(target=lambda: self._slot(*args, **kwargs)).start()
