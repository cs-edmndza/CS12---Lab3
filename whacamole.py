# pyright: strict

from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum, auto
from random import Random
from typing import Protocol


class MoleState(StrEnum):
    INACTIVE = 'inactive'
    ACTIVE = 'active'
    HIT = 'hit'


class Mole(Protocol):
    active_turns: int
    hit_points: input

    @property
    def base_hit_points(self):
        return self._base_hit_points

    @property
    def base_turns_active(self):
        return self.base_turns_active

    @property
    def points(self):
        return self._points

    @property
    def state(self):
        return self._state

    def spawn(self):
        self._state = MoleState.INACTIVE
        self._hit_points = self._base_hit_points
        self._active_turns = self._base_turns_active

    def pop_up(self):
        self._state = MoleState.ACTIVE

    def hide(self):
        self._state = MoleState.INACTIVE

    def receive_hit(self):
        self._state = MoleState.HIT

    def update_next_turn_state(self):
        if self._state == MoleState.ACTIVE:
            self._state = MoleState.INACTIVE
        elif self._state == MoleState.INACTIVE:
            self._state = MoleState.ACTIVE
        else:
            self._state = MoleState.HIT

class WhacAMoleModel:
    def __init__(self, config, hammer):
        self._config = config
        self._hammer = _hammer

    def _turn(self):
        return self._turn

    def _moles(self):
        return self._moles

    def _total_points(self):
        return self._total_points

    def _is_game_over(self):
        return self._is_game_over

    @property
    def moles(self):
        return self._moles

    @property
    def current_turn(self):
        return self._turn

    @property
    def is_game_over(self):
        return self._is_game_over

    def process_hit(self, idx: int):


    def start_turn(self):

    def finish_turn(self):

class WhacAMoleConfig:
    def __init__(self, mole_counts, turns, rng):
        self._mole_counts = mole_counts
        self._turns = turns
        self._rng = rng

class Hammer(Protocol):
    power: int
    width: int




class WhacAMoleView:
    def ask_for_hole_to_hit(self):
        return int(input('Enter the hole you want to whack'
                         ' (0-indexed): '))

    def display_turn(self, model: WhacAMoleModel):
        print(f'Turn {model.current_turn}')
        print(f'Points: {model.points}')
        print(' '.join([self._display_mole(mole) for mole in model.moles]))
        # print(' '.join([str(i) for i in range(len(model.moles))]))

    def _display_mole(self, mole: Mole) -> str:
        match mole.state:
            case MoleState.INACTIVE:
                return '_'
            case MoleState.HIT:
                return 'x'
            case MoleState.ACTIVE:
                return '🟤'
            case _:
                raise ValueError


class WhacAMoleController:
    def __init__(self, model: WhacAMoleModel, view: WhacAMoleView):
        self._model = model
        self._view = view

    def start(self):
        model = self._model
        view = self._view

        while not model.is_game_over:
            model.start_turn()
            view.display_turn(model)
            idx = view.ask_for_hole_to_hit()
            model.process_hit(idx)
            view.display_turn(model)
            model.finish_turn()

