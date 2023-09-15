from typing import Optional
import tcod
import tcod.event as te
from actions import Action, EscapeAction, MovementAction


class EventHandler(te.EventDispatch[Action]):
    def ev_quit(self, event: te.Quit) -> Optional[Action]:
        raise SystemExit()
    
    def ev_keydown(self, event: te.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        match key:
            case te.KeySym.UP:
                action = MovementAction(dx=0, dy=-1)
            case te.KeySym.DOWN:
                action = MovementAction(dx=0, dy=1)
            case te.KeySym.LEFT:
                action = MovementAction(dx=-1, dy=0)
            case te.KeySym.RIGHT:
                action = MovementAction(dx=1, dy=0)
            case te.KeySym.ESCAPE:
                action = EscapeAction()

        return action