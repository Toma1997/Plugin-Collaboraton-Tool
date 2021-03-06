from plugin_framework.plugin import Plugin
from .widgets.tasks_tool import TasksTool
from .label.label_service import LabelService
from .task.task_service import TaskService

class Main(Plugin):
    """
    Klasa koja predstavlja konkretni plugin. Nasledjujemo "apstraktnu" klasu Plugin.
    Ova klasa predstavlja plugin za aplikaciju zahteva o razvoju softvera.
    """
    def __init__(self, spec):
        """
        Inicijalizator Razvoj Softvera plugina.

        :param spec: specifikacija metapodataka o pluginu.
        :type spec: dict
        """
        super().__init__(spec)

    def get_widget(self, parent=None):
        """
        Ova metoda vraca konkretni widget koji ce biti smesten u centralni deo aplikacije i njenog 
        glavnog prozora. Može da vrati toolbar, kao i meni, koji će biti smešten u samu aplikaciju.
        
        :param parent: bi trebao da bude widget u koji će se smestiti ovaj koji naš plugin omogućava.
        :returns: QWidget, QToolbar, QMenu
        """
        task_service = TaskService()
        task_service.load_tasks()
        label_service = LabelService()
        label_service.load_labels()
        
        return TasksTool(task_service, label_service, parent), None, None