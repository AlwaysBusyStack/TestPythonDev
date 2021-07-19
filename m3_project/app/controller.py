from m3.actions import ControllerCache
from objectpack.observer import (
    ObservableController,
    Observer,
)

observer = Observer()
# observer._model_register = ControllerCache.get_controllers()
controller = ObservableController(
    url='actions',
    observer=observer,
)

