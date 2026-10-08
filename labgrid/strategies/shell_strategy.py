"""Strategy mínima: off -> shell (power cycle + login en consola serie)."""
import enum

import attr
from labgrid import step, target_factory
from labgrid.strategy import Strategy, StrategyError


class Status(enum.Enum):
    unknown = 0
    off = 1
    shell = 2


@target_factory.reg_driver
@attr.s(eq=False)
class ShellStrategy(Strategy):
    bindings = {
        "power": "PowerProtocol",
        "shell": "ShellDriver",
    }
    status = attr.ib(default=Status.unknown)

    @step(args=["status"])
    def transition(self, status, *, step):
        if not isinstance(status, Status):
            status = Status[status]
        if status == Status.unknown:
            raise StrategyError(f"can not transition to {status}")
        if status == self.status:
            step.skip("nothing to do")
            return
        if status == Status.off:
            self.target.deactivate(self.shell)
            self.power.off()
        elif status == Status.shell:
            self.power.cycle()
            self.target.activate(self.shell)
        self.status = status
