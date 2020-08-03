# Import modules
import Impulse.tools.SMS.sendRequest as request
import Impulse.tools.SMS.randomData as randomData

__services = request.getServices()


def flood(target):
    # Get services list
    service = randomData.random_service(__services)
    service = request.Service(service)
    service.sendMessage(target)
